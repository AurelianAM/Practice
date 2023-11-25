import os

def deleteFile(file_path):
    # Check if the file exists before attempting to delete it
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"File '{file_path}' has been deleted.")
    else:
        print(f"File '{file_path}' does not exist.")

if __name__ == "__main__":
    deleteFile("output.mp4")