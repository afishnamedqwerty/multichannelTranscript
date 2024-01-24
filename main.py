import os
import subprocess
import shutil
from audio_converters import convert_aac_to_flac, convert_mp3_to_flac, convert_wav_to_flac

def check_file_extensions(folder):
    extensions = set()
    for file_name in os.listdir(folder):
        ext = os.path.splitext(file_name)[1]
        extensions.add(ext.lower())
    return extensions

def clear_and_copy_to_flac_cache(source_folder, flac_cache_folder):
    if os.path.exists(flac_cache_folder):
        shutil.rmtree(flac_cache_folder)
    os.makedirs(flac_cache_folder)

    for file_name in os.listdir(source_folder):
        if file_name.endswith('.flac'):
            shutil.copy2(os.path.join(source_folder, file_name), flac_cache_folder)

def run_script(script_name):
    """Run a Python script using subprocess."""
    try:
        completed_process = subprocess.run(['python', script_name], check=True, text=True, capture_output=True)
        print(f"Output of {script_name}:\n{completed_process.stdout}")
    except subprocess.CalledProcessError as e:
        print(f"Error in {script_name}: {e.stderr}")

def main():
    data_folder = '/data'
    flac_cache = 'flac_cache'

    extensions = check_file_extensions(data_folder)

    if extensions == {'.flac'}:
        clear_and_copy_to_flac_cache(data_folder, flac_cache)
    else:
        for file_name in os.listdir(data_folder):
            if file_name.endswith('.aac'):
                convert_aac_to_flac(data_folder, flac_cache)
            elif file_name.endswith('.mp3'):
                convert_mp3_to_flac(data_folder, flac_cache)
            elif file_name.endswith('.wav'):
                convert_wav_to_flac(data_folder, flac_cache)




    """Main function to run scripts sequentially."""
    run_script('whisper_binaries.iterate.py')
    run_script('multichannel_parser.py')

if __name__ == "__main__":
    main()
