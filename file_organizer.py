import os
import shutil

def organize_folder(folder_path):
    if not os.path.exists(folder_path):
        print("Folder does not exist.")
        return
    total_files_moved=0
    for file in os.listdir(folder_path):
        file_full_path = os.path.join(folder_path, file)

        if os.path.isfile(file_full_path):

            # Check if file has extension
            if "." in file:
                extension = file.split(".")[-1].lower()
            else:
                extension = "no_extension"

            new_folder = os.path.join(folder_path, extension)

            if not os.path.exists(new_folder):
                os.makedirs(new_folder)

            shutil.move(file_full_path, os.path.join(new_folder, file))
            total_files_moved+=1

    print("Files organized successfully.")
    print("Total files moved:",total_files_moved)

if __name__ == "__main__":
    folder = input("Enter folder path to organize: ")
    organize_folder(folder)