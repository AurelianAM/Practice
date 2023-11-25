import subprocess
from delete_file import deleteFile

def compress(compressed_file):
    # Define the FFmpeg command as a list of arguments
    ffmpeg_command = [
        'ffmpeg',
        '-i', 'output.mp4',
        '-c:v', 'h264_nvenc',
        '-b:v', '1000k',
        '-c:a', 'aac',
        '-strict', 'experimental',
        f'{compressed_file}.mp4'
    ]

    # Run the FFmpeg command
    try:
        subprocess.run(ffmpeg_command, check=True)
        print("Compression completed successfully.")
        deleteFile("output.mp4")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
