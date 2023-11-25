import glob
import os
import subprocess

def concatenate_video_files_in_order_by_name_without_processes(folder_path, output_file="output.mp4"):
  """Concatenates all video files in the specified folder in order by name into a single MP4 file, without using processes.

  Args:
    folder_path: The path to the folder containing the video files to concatenate.
    output_file: The path to the output MP4 file. Defaults to "output.mp4".
  """

  # Get a list of all video files in the folder, sorted by name.
  video_files = sorted(glob.glob(f"{folder_path}/*.ts"))

  # Open the output file for writing.
  with open(output_file, "wb") as output_file:

    # For each video file, open the file for reading and copy the contents to the output file.
    for video_file in video_files:
      with open(video_file, "rb") as input_file:
        output_file.write(input_file.read())

if __name__ == "__main__":
  TEMP_FOLDER = "downloaded_videos"
  # Concatenate all video files in the current folder in order by name into a single MP4 file named output.mp4.
  concatenate_video_files_in_order_by_name_without_processes(TEMP_FOLDER)