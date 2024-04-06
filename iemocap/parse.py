import os
import glob
import re
import json


# Loop over the range
for i in range(1, 2):
    # Outer dictionary to store filepaths as keys
    outer_dict = {}
    # Construct the folder path
    folder_path = f"data/iemocap/Session{i}/dialog/EmoEvaluation"

    # Loop over each .txt file in the folder
    for txt_file in glob.glob(os.path.join(folder_path, "*.txt")):
        # Inner dictionary to store values by their name as a key
        # inner_dict = {}
        # Get the base name of the txt_file
        base_name = os.path.basename(txt_file)

        # Construct the path to the corresponding file in the transcriptions folder
        transcriptions_file_path = (
            f"data/iemocap/Session{i}/dialog/transcriptions/{base_name}"
        )

        line_values = {}

        # Open the .txt file
        with open(txt_file, "r") as file:
            # Read the file line by line
            lines = file.readlines()

            # Loop over the lines
            counter = 0

            for line in lines:
                # Check if the line starts with "["
                if line.startswith("["):
                    # Reset the counter
                    counter = 3
                    # Split the line on white space
                    match = re.match(
                        r"(\[.*?\])\s+(Ses.*?)\s+(\w{3})\s+(\[.*?\])", line
                    )
                    if not match:
                        raise ValueError("no good")
                    components = match.groups()
                    # Check if the components are as expected
                    if not len(components) == 4:
                        print(components)
                        raise ValueError("why")
                    if len(components) == 4:
                        timestamp, audio_file_path, emotion, intensity = components
                        new_dict = dict()
                        # Store the values by their name as a key in the inner dictionary
                        new_dict["timestamp"] = timestamp
                        new_dict["audio_file_path"] = audio_file_path
                        new_dict["full_audio_file_path"] = (
                            f"data/iemocap/Session{i}/sentences/wav/{audio_file_path}.wav"
                        )
                        new_dict["emotion"] = emotion
                        new_dict["intensity"] = intensity
                        line_values[audio_file_path] = new_dict
                elif counter > 0:
                    # Capture the line value into the new_dict
                    line_values[audio_file_path][f"rating{counter}"] = line.split("\t")[
                        1
                    ].strip(";")
                    if counter == 1:
                        line_values[audio_file_path]
                    counter -= 1

        outer_dict[txt_file] = line_values

        # Open the transcriptions file
        with open(transcriptions_file_path, "r") as transcriptions_file:
            # Read the file line by line
            transcriptions_lines = transcriptions_file.readlines()

            # Loop over the lines
            for line in transcriptions_lines:
                # Split the line into components
                match = re.match(r"(Ses.*?)\s+(\[.*?\]:)\s+(.*)", line)

                if not match:
                    print(f"No match found in line: {line}")
                    continue
                    # raise ValueError("No match found in line: " + line)

                # Extract the matched strings
                components = match.groups()

                # Check if the components are as expected
                if len(components) != 3:
                    raise ValueError("Unexpected number of components in line: " + line)

                transcription_audio_file_path, timestamp, text = components

                # Access the object using the audio_file_path as the key
                value_obj = outer_dict[txt_file][transcription_audio_file_path]

                # Store the text in the dictionary
                value_obj["text"] = text

        # Store the inner dictionary in the outer dictionary where its filepath is the key
    # outer_dict["files"] = inner_dict

    with open(f"session{i}.json", "w") as f:
        json.dump(outer_dict, f)
