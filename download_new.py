import requests
import os
import concurrent.futures


def download_video_segment(url, index, download_directory):
    """Downloads a video segment from the specified URL and saves it to the specified download directory with the specified filename.

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

    def resume_download(filename, url):
        file_size = os.path.getsize(filename)
        headers = {
            "Range": f"bytes={file_size}-"
        }

        response = requests.get(url, headers=headers)
        check_status(response)

        with open(filename, "ab") as file:
            file.write(response.content)

    try:
        filename = f"{index:04d}.ts"
        filepath = os.path.join(download_directory, filename)

        if os.path.exists(filepath):
            # Resume download
            resume_download(filename, url)
        else:
            # Start new download
            response = requests.get(url)
            check_status(response)

            with open(filepath, "wb") as file:
                progress_bar(response.headers["Content-Length"], 0)
                file.write(response.content)

        print(f"Downloaded {filename}")
    except Exception as e:
        print(f"Error downloading {url}: {str(e)}")

def download_videos(url_list, download_directory):
    os.makedirs(download_directory, exist_ok=True)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for index, url in enumerate(url_list):
            futures.append(executor.submit(download_video_segment, url, index, download_directory))
        
        # Wait for all downloads to complete
        concurrent.futures.wait(futures)
    
    print("Download finished...")