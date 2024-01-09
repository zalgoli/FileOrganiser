import os
import shutil
import argparse

def organise_files(input_folder):

    # Initial list of all files in input folder
    files = [file for file in os.listdir(input_folder) if os.path.isfile(os.path.join(input_folder, file))]

    file_dict = {}

    for file in files:
        _, extension = os.path.splitext(file)
        # Removing leading dot
        extension = extension[1:]

        if extension not in file_dict:
            os.makedirs(os.path.join(input_folder, extension), exist_ok = True)
            file_dict[extension] = []

        # Moving to corresponding file
        source_path = os.path.join(input_folder, file)
        target_path = os.path.join(input_folder, extension, file)
        shutil.move(source_path, target_path)

        # Updating dictionary
        file_dict[extension].append(file)

        print("Organised files into folders.")
        for extension, files in file_dict.items():
            print(f"{extension.upper()} folder: {len(files)} files")

def main():
    parser = argparse.ArgumentParser(description= "Organise files into different folders based on extensions")
    parser.add_argument("input_folder", help= "Path of the folder to organise")

    args = parser.parse_args()
    organise_files(args.input_folder)

if __name__ == "__main__":
    main()