import requests
import os
from moviepy.editor import VideoFileClip, concatenate_videoclips
import concurrent.futures

def download_video_segment(url, index, download_directory):
    try:
        response = requests.get(url)

        if response.status_code == 200:
            filename = f"{index}.ts"
            filepath = os.path.join(download_directory, filename)

            with open(filepath, "wb") as file:
                file.write(response.content)

            print(f"Downloaded {filename}")
        else:
            print(f"Failed to download {url}: Status code {response.status_code}")
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

def convert_ts_to_avi(ts_files, download_directory, output_filename, max_processes=5):
    def convert_file(ts_file):
        try:
            input_filepath = os.path.join(download_directory, ts_file)
            clip = VideoFileClip(input_filepath)
            return clip
        except Exception as e:
            print(f"Error converting {ts_file} to AVI: {str(e)}")
            return None
    
    video_clips = []
    with concurrent.futures.ThreadPoolExecutor(max_processes) as executor:
        futures = [executor.submit(convert_file, ts_file) for ts_file in ts_files]
        
        for future in concurrent.futures.as_completed(futures):
            clip = future.result()
            if clip:
                video_clips.append(clip)
    
    final_clip = concatenate_videoclips(video_clips, method="compose")
    final_clip.write_videofile(output_filename, codec="mpeg4")

if __name__ == "__main__":
    urlList = [f"https://5e6f49934c5f8.streamlock.net:4443/vod/_definst_/2022/20221101173000ROC3_RO/20221101173000ROC3_RO_aac.mp4/media_w188600440_{i}.ts?hash=7ce3e674b65c24a34a9e0ed1347995588e545001"
               for i in range(1180)]
    
    download_directory = "downloaded_videos"
    output_filename = "output.avi"
    
    # download_videos(urlList, download_directory)
    
    ts_files = [f"{i}.ts" for i in range(1180)]  # Assuming all .ts files are in sequence
    convert_ts_to_avi(ts_files, download_directory, output_filename, max_processes=5)
    
    print("Video concatenation and conversion to AVI completed.")
