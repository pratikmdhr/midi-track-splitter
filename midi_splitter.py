import os

import mido
from mido import MidiFile, MidiTrack


def split_midi(input_file):
    # Load the MIDI file
    mid = MidiFile(input_file)

    # Extract the base name of the input MIDI file (without extension)
    base_name = os.path.splitext(os.path.basename(input_file))[0]

    # Create an "output" directory if it doesn't exist
    output_directory = "output"
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Iterate over tracks in the MIDI file
    for i, track in enumerate(mid.tracks):
        # Attempt to find a track name in the track's events
        track_name = None
        for msg in track:
            if msg.type == "track_name":
                track_name = msg.name
                break

        # Use a default name if no track name is found
        if track_name is None or track_name == "":
            track_name = f"Track_{i}"

        # Replace problematic characters in the filename
        safe_track_name = track_name.replace("/", "-").replace("\\", "-")

        # Combine the base name and track name for the output file name
        output_dir_path = os.path.join(output_directory, base_name)
        os.makedirs(
            output_dir_path, exist_ok=True
        )  # Create nested directory if it doesn't exist
        output_file_name = f"{base_name}_{safe_track_name}.mid"
        output_file = os.path.join(output_dir_path, output_file_name)

        # Create a new MIDI file with a single track
        new_mid = MidiFile()
        new_track = MidiTrack()
        new_mid.tracks.append(new_track)

        # Copy messages from the original track to the new track
        for msg in track:
            new_track.append(msg)

        # Save the new MIDI file in the output directory
        new_mid.save(output_file)
        print(f'Track {i} saved as "{output_file}"')


def process_midi_files_in_directory(parent_directory):
    # Recursively search for .mid files in the specified directory and its subdirectories
    for root, _, files in os.walk(parent_directory):
        for file in files:
            if file.endswith(".mid"):
                midi_file_path = os.path.join(root, file)
                split_midi(midi_file_path)


if __name__ == "__main__":
    # Ask the user for the path to the parent folder
    parent_folder_input = input(
        "Enter the path to the parent folder (Press Enter for current working directory): "
    )

    # Use the current working directory if the user hits Enter without entering anything
    parent_folder = parent_folder_input.strip() or os.getcwd()

    # Process all .mid files in the specified directory and its subdirectories
    process_midi_files_in_directory(parent_folder)
