import os
import concurrent.futures
import requests
from urllib.parse import urlparse, parse_qs
import glob
import subprocess
from shutil import rmtree

class Video():

    def __init__(self, id, url, videoName):
        self.id = f"{id:03d}"
        self.url = url
        self.videoName = videoName + ".ts"
        self.download_folder = self.id + "_" + self.videoName + "download"
        self.scheme, self.host, self.path_segments, self.query, self.query_params, self.file_name = self.__parseMyURL()
        self.maxFiles = self.__getMaxFiles()
    
    def __getMaxFiles(self):
        file_name = self.file_name
        length = int((file_name.split("_")[-1]).split(".")[0])
        return length

    def __parseMyURL(self):
        parsed_url = urlparse(self.url)
        # Extract components
        scheme = parsed_url.scheme
        host = parsed_url.netloc
        path = parsed_url.path
        query = parsed_url.query
        # Extract path segments
        path_segments = path.split('/')
        # Extract query parameters
        query_params = parse_qs(query)
        file_name = path_segments[-1]
        return scheme, host, path_segments, query, query_params, file_name

    def __downloadURLGenerator(self):
        for i in range(self.maxFiles + 1):
        # for i in range(20, 30):
            u = f"{self.scheme}://{self.host}{"/".join(self.path_segments[0:len(self.path_segments) - 1])}/"
            rootFile_list = self.file_name.split("_")
            rootFile = "_".join(rootFile_list[:len(rootFile_list) - 1])
            u += rootFile
            u += f"_{i}.ts?hash={self.query_params['hash'][0]}"
            yield u

    def __downloadVideoSegment(self, url, index):
        """Downloads a video segment from the specified URL and saves it to the specified download directory with the specified videoName.

        Args:
            url: The URL of the video segment to download.
            index: The index of the video segment.
            download_directory: The path to the download directory.
        """
        def check_status(response):
            if response.status_code != 200:
                raise Exception(f"Failed to download {url}: Status code {response.status_code}")
        def progress_bar(total_size, downloaded_size):
            progress = int(downloaded_size) // int(total_size)
            print(f"Downloading {url}: {progress:.2%}")
        def resume_download(videoName, url):
            file_size = os.path.getsize(videoName)
            headers = {"Range": f"bytes={file_size}-"}
            response = requests.get(url, headers=headers)
            check_status(response)
            with open(videoName, "ab") as file:
                file.write(response.content)
        try:
            videoName = f"{index:04d}.ts"
            filepath = os.path.join(self.download_folder, videoName)
            if os.path.exists(filepath):
                # Resume download
                resume_download(videoName, url)
            else:
                # Start new download
                response = requests.get(url)
                check_status(response)
                with open(filepath, "wb") as file:
                    progress_bar(response.headers["Content-Length"], 0)
                    file.write(response.content)
            print(f"Downloaded {videoName}")
        except Exception as e:
            print(f"Error downloading url: {str(e)}")

    def __downloadVideo(self):
        os.makedirs(self.download_folder, exist_ok=True)
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = []
            for index, url in enumerate(self.__downloadURLGenerator()):
                futures.append(executor.submit(self.__downloadVideoSegment, url, index))         
            # Wait for all downloads to complete
            concurrent.futures.wait(futures)
        print("Download finished...")

    def __deleteDownloadFolder(self):
            rmtree(self.download_folder)

    def __concatenateVideoParts(self):
        output_file = self.videoName
        # Get a list of all video files in the folder, sorted by name.
        video_files = sorted(glob.glob(f"{self.download_folder}/*.ts"))
        # Open the output file for writing.
        with open(output_file, "wb") as output_file:
            # For each video file, open the file for reading and copy the contents to the output file.
            for video_file in video_files:
                with open(video_file, "rb") as input_file:
                    output_file.write(input_file.read())
        self.__deleteDownloadFolder()
    
    def __compress(self):
        input_video = self.videoName
        output_video = input_video.split(".")[0] + "_compressed.mp4"
        # Define the FFmpeg command as a list of arguments
        command = [
            'ffmpeg',
            '-i', input_video,  # Input .ts file
            '-c:v', 'libx264',  # Video codec (H.264)
            # '-preset', 'ultrafast',  # Preset for speed/quality trade-off
            # '-crf', '23',  # Constant Rate Factor (lower is better quality)
            # '-c:a', 'aac',  # Audio codec (AAC)
            output_video  # Output .mp4 file
        ]

        # Run the ffmpeg command
        try:
            subprocess.run(command, check=True)
            print(f"Compression and conversion completed. Output saved as {output_video}")
        except subprocess.CalledProcessError as e:
            print(f"Error: {e}")

    def getVideoFile(self, concatenate = True, compress = False):
        self.__downloadVideo()
        if concatenate:
            self.__concatenateVideoParts()
            if compress:
                self.__compress()

if __name__ == "__main__":
    print()
    video1 = Video(1, "https://5aa64ca8b95b8.streamlock.net:4443/vod/_definst_/2023/20230413173000ROC3_RO/20230413173000ROC3_RO_aac.mp4/media_w450690834_1158.ts?hash=3a0e0964f395e0987f5f040317ce556e9988799e", "WebAppBuild_7")
    video1.getVideoFile(compress=True)