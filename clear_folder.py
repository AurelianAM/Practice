import os

def clearFolder(folder_path):
    # List all files in the folder
    files = os.listdir(folder_path)

    # Iterate through the files and delete them
    for file in files:
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path):
            os.remove(file_path)

    print(f"All files in '{folder_path}' folder have been deleted.")

if __name__ == "__main__":
    clearFolder("downloaded_videos")