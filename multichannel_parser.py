import os
import re
import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


def read_srt_files(folder_path):
    transcripts = []
    for file in os.listdir(folder_path):
        if file.endswith(".srt"):
            file_path = os.path.join(folder_path, file)
            print("Filepath:  " + file_path + "\n")
            try:
                with open(file_path, 'r') as f:
                    content = f.read()
                    transcripts.append((file, content))
                    logging.info(f"File read successfully: {file}")
            except Exception as e:
                logging.error(f"Error reading file {file}: {e}")
    return transcripts

def parse_filename(file_name):
    # Remove the prefix (number and hyphen)
    file_name = re.sub(r'^\d+-', '', file_name)
    # Remove all characters after "_"
    file_name = re.sub(r'_.*', '', file_name)
    return file_name

def parse_srt_content(file_name, content):
    file_name = parse_filename(file_name)
    pattern = re.compile(r'(\d+)\n(\d{2}:\d{2}:\d{2},\d{3}) --> (\d{2}:\d{2}:\d{2},\d{3})\n(.*?)\n\n', re.DOTALL)
    try:
        matches = pattern.findall(content)
        parsed_content = [(file_name, start, text.strip()) for _, start, _, text in matches]
        logging.info(f"Content parsed successfully for file: {file_name}")
        return parsed_content
    except Exception as e:
        logging.error(f"Error parsing content for file {file_name}: {e}")
        return []


def merge_and_sort_transcripts(transcripts):
    all_transcripts = []
    for file_name, content in transcripts:
        all_transcripts.extend(parse_srt_content(file_name, content))
    all_transcripts.sort(key=lambda x: x[1])
    logging.info("Transcripts merged and sorted successfully" + str(all_transcripts))
    return all_transcripts


def write_to_file(transcripts, transcripts_folder):
    #output_file = ''
    try:
        # Find the maximum length of filenames
        max_filename_length = max(len(filename) for filename, _, _ in transcripts)
        if not os.path.exists(transcripts_folder):
            os.makedirs(transcripts_folder)

        # Format current date for filename
        current_date = datetime.date.today().strftime("%Y-%m-%d")
        output_file = os.path.join(transcripts_folder, f"{current_date}-meeting_notes.txt")

        with open(output_file, 'w') as f:
            for file_name, timestamp, text in transcripts:
                # Calculate the number of tabs needed
                tab_count = (max_filename_length - len(file_name)) // 4 + 1
                tabs = '\t' * tab_count

                # Write to file with the calculated tabs
                f.write(f'{timestamp} {file_name}{tabs}: {text}\n')

        logging.info(f"Output file written successfully: {output_file}")
    except Exception as e:
        logging.error(f"Error writing to output file: {e}")




def read_and_parse_files(directory):
    all_records = []
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            with open(os.path.join(directory, filename), 'r') as file:
                for line in file:
                    match = re.search(r'(\d{2}:\d{2}:\d{2})\s+(.*)', line)
                    if match:
                        timestamp = match.group(1)
                        message = match.group(2)
                        all_records.append((timestamp, message, filename))
    return all_records

def sort_records(all_records):
    return sorted(all_records, key=lambda x: datetime.strptime(x[0], '%H:%M:%S'))

def write_to_transcript(sorted_records, output_file):
    with open(output_file, 'w') as file:
        for record in sorted_records:
            file.write(f"{record[0]} {record[1]} (from {record[2]})\n")

def main():
    folder_path = 'srt_cache'
    #output_file = 'merged_transcript.txt'
    transcripts_folder = 'transcripts'
    transcripts = read_srt_files(folder_path)
    merged_transcripts = merge_and_sort_transcripts(transcripts)
    write_to_file(merged_transcripts, transcripts_folder)

if __name__ == "__main__":
    main()


