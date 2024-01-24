'''import os
import subprocess

def process_flac_files(source_folder, dest_folder):
    # Check if destination folder exists, create if not
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    # Temporary folder for all outputs
    temp_folder = 'temp_output'
    if not os.path.exists(temp_folder):
        os.makedirs(temp_folder)
    
    # Process each .flac file
    for filename in os.listdir(source_folder):
        if filename.endswith(".flac"):
            source_file = os.path.join(source_folder, filename)
            output_filename = f"output_{os.path.splitext(filename)[0]}.txt"
            output_file = os.path.join(dest_folder, output_filename)
            command = f"whisper {source_file} --model small > {output_file}"

            try:
                subprocess.run(command, shell=True, check=True)
                print(f"Processed: {filename}")
            except subprocess.CalledProcessError as e:
                print(f"Error processing {filename}: {e}")

# Replace these paths with your actual folder paths
source_folder = 'audio_cache'
dest_folder = 'text_cache'
process_flac_files(source_folder, dest_folder)'''

import os
import subprocess
import shutil

def process_flac_files(source_folder, srt_folder):
    # Check if srt folder exists, create if not
    if not os.path.exists(srt_folder):
        os.makedirs(srt_folder)

    # Temporary folder for all outputs
    temp_folder = 'temp'
    if not os.path.exists(temp_folder):
        os.makedirs(temp_folder)

    # Process each .flac file
    for filename in os.listdir(source_folder):
        if filename.endswith(".flac"):
            source_file = os.path.join(source_folder, filename)
            temp_output_file = os.path.join(temp_folder, os.path.splitext(filename)[0])
            srt_file = os.path.join(srt_folder, os.path.splitext(filename)[0] + '.srt')
            command = f"whisper {source_file} --model small --output {temp_output_file}"

            try:
                subprocess.run(command, shell=True, check=True)
                # Move the .srt file to srt_folder
                if os.path.exists(temp_output_file + '.srt'):
                    shutil.move(temp_output_file + '.srt', srt_file)
                print(f"Processed and stored SRT: {filename}")
            except subprocess.CalledProcessError as e:
                print(f"Error processing {filename}: {e}")

            # Cleanup: Delete the temporary output folder
            if os.path.exists(temp_folder):
                shutil.rmtree(temp_folder)

# Replace these paths with your actual folder paths
source_folder = 'flac_cache'
srt_folder = 'srt_cache'
process_flac_files(source_folder, srt_folder)

