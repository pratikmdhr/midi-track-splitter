# MIDI Track Splitter

This Python script splits MIDI files into separate tracks.

## Requirements

- Python 3.x
- Mido: MIDI Objects for Python. You can install it with pip: `pip install mido`

## Usage

1. Clone the repository or download the `midi_splitter.py` file.
2. Open a terminal/command prompt.
3. Navigate to the directory containing `midi_splitter.py`.
4. Run the script using the command `python3 midi_splitter.py`.
5. When prompted, enter the path to the parent folder containing the MIDI files you want to split. If you have the midi files stored in current working directory, simply press Enter.

The script will recursively search for .mid files in the specified directory and its subdirectories, split them into separate tracks, and save the new MIDI files in an "output" directory.
