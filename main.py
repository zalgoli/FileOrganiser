import os
import shutil

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

if __name__ == "__main__":
    input_folder = input("Enter the path of the file to organise: ")
    organise_files(input_folder)