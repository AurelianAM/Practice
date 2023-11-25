import subprocess
import glob
import os
from clear_folder import clearFolder

def concatenare(video_folder):
    # Get a list of .ts files in the 'downloaded_videos' directory
    ts_files = glob.glob(f'{video_folder}/*.ts')

    # Construct the ffmpeg command
    ffmpeg_command = [
        'ffmpeg',
        '-i', f'concat:{ "|".join(ts_files) }',
        '-c', 'copy',
        '-bsf:a', 'aac_adtstoasc',
        'output.mp4'
    ]

    # Run the ffmpeg command
    try:
        subprocess.run(ffmpeg_command, check=True)
        print("Conversion completed successfully!")
        clearFolder(video_folder)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

def concatenate_video_files_in_order(video_files: list[str], output_file: str):
  """Concatenates the video files in the specified order into a single MP4 file.

  Args:
    video_files: A list of video files to concatenate.
    output_file: The path to the output MP4 file.
  """

  # Create a temporary file to store the FFmpeg command.
  with open("/tmp/ffmpeg_command.txt", "w") as f:
    for video_file in video_files:
      f.write(f"-i {video_file}\n")

  # Concatenate the video files using the FFmpeg command.
  subprocess.run(["ffmpeg", "-f", "concat", "-safe", "0", "-i", "/tmp/ffmpeg_command.txt", output_file], check=True)

  # Delete the temporary file.
  os.remove("/tmp/ffmpeg_command.txt")