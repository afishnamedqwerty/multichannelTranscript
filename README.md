# Whisper Non-Diarized Multi-Channel Transcription tool

## Introduction
The Multi-Channel Transcription tool is designed to automate the transcription of multiple audio files into a singular written transcript. It utilizes Whisper binaries to process `.flac` audio files, generating corresponding `.srt` files that are then merged using timestamp and filename to denote an ordered transcript between multiple simultaneous audio channels. This transcript is output in .txt format.

## Features
- **Automated Processing**: Converts `.aac`, `.mp3`, and `.wav` audio files to `.flac` format automatically.
- **Batch Processing**: Capable of handling multiple files in a single run.
- **Customizable Output**: Transcriptions are stored in a designated `transcripts` folder.

## Prerequisites
Before using this project, ensure you have the following installed:
- Python 3.x
- Whisper binaries and installation instructions (https://github.com/openai/whisper)

## Installation
1. Clone this repository to your local machine.
2. Ensure Python 3.x is installed.
3. Install Whisper binaries following their official documentation.

## Usage
1. Place your audio files into the `data` folder (`.aac`, `.flac`, `.mp3`, `.wav` supported).
2. Run the script using Python: `python main.py`.
3. Audio files are converted and copied into `flac_cache` folder and whisper transcription is sequentially run on each file. 
4. Whisper flag customization is available in the `whisper_binaries_iterate.py` file by editing the following command with supported Whisper configurations: `command = f"whisper {source_file} --model small --output {temp_output_file}"` Secondary output files for each audio file are cleaned upon completion and processed SRT files are stored into the `srt_cache` folder.
5. Upon successful completion of whisper transcription, the `multichannel_parser.py` script is called within `main.py` to merge and format all audio transcripts into one ordered text file.


## Folder Structure
- `data/`: Place your supported audio files here.
- `flac_cache/`: Temp folder to load the converted `.flac` files for processing. 
- `srt_cache/`: Processed `.srt` files will be stored here.
- `transcripts/`: Output location for rendered transcripts.

