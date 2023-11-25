import requests
import os
from moviepy.editor import VideoFileClip, concatenate_videoclips

# """
# https://5e6f49934c5f8.streamlock.net:4443/vod/_definst_/2022/20221101173000ROC3_RO/20221101173000ROC3_RO_aac.mp4/media_w188600440_10.ts?hash=7ce3e674b65c24a34a9e0ed1347995588e545001
# https://5e6f49934c5f8.streamlock.net:4443/vod/_definst_/2022/20221101173000ROC3_RO/20221101173000ROC3_RO_aac.mp4/media_w188600440_18.ts?hash=7ce3e674b65c24a34a9e0ed1347995588e545001
# https://5e6f49934c5f8.streamlock.net:4443/vod/_definst_/2022/20221101173000ROC3_RO/20221101173000ROC3_RO_aac.mp4/media_w188600440_508.ts?hash=7ce3e674b65c24a34a9e0ed1347995588e545001
# https://5e6f49934c5f8.streamlock.net:4443/vod/_definst_/2022/20221101173000ROC3_RO/20221101173000ROC3_RO_aac.mp4/media_w188600440_1132.ts?hash=7ce3e674b65c24a34a9e0ed1347995588e545001
# """

# url = "https://5e6f49934c5f8.streamlock.net:4443/vod/_definst_/2022/20221101173000ROC3_RO/20221101173000ROC3_RO_aac.mp4/media_w188600440_1179.ts?hash=7ce3e674b65c24a34a9e0ed1347995588e545001"


def download_videos(url_list, download_directory):
    os.makedirs(download_directory, exist_ok=True)
    
    for index, url in enumerate(url_list):
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

def combine_ts_to_avi(download_directory, output_filename):
    ts_files = [f for f in os.listdir(download_directory) if f.endswith(".ts")]
    ts_files.sort(key=lambda x: int(x.split('.')[0]))

    video_clips = [VideoFileClip(os.path.join(download_directory, ts_file)) for ts_file in ts_files]
    final_clip = concatenate_videoclips(video_clips, method="compose")
    final_clip.write_videofile(output_filename, codec="mpeg4")

if __name__ == "__main__":
    urlList = [f"https://5e6f49934c5f8.streamlock.net:4443/vod/_definst_/2022/20221101173000ROC3_RO/20221101173000ROC3_RO_aac.mp4/media_w188600440_{i}.ts?hash=7ce3e674b65c24a34a9e0ed1347995588e545001"
               for i in range(1180)]
    
    # urlList = ["https://5e6f49934c5f8.streamlock.net:4443/vod/_definst_/2022/20221101173000ROC3_RO/20221101173000ROC3_RO_aac.mp4/media_w188600440_10.ts?hash=7ce3e674b65c24a34a9e0ed1347995588e545001",
            #    "https://5e6f49934c5f8.streamlock.net:4443/vod/_definst_/2022/20221101173000ROC3_RO/20221101173000ROC3_RO_aac.mp4/media_w188600440_100.ts?hash=7ce3e674b65c24a34a9e0ed1347995588e545001"]

    download_directory = "downloaded_videos"
    output_filename = "output.avi"
    
    download_videos(urlList, download_directory)
    combine_ts_to_avi(download_directory, output_filename)
    
    print("Video concatenation and conversion to AVI completed.")










# urlList = [f"https://5e6f49934c5f8.streamlock.net:4443/vod/_definst_/2022/20221101173000ROC3_RO/20221101173000ROC3_RO_aac.mp4/media_w188600440_{i}.ts?hash=7ce3e674b65c24a34a9e0ed1347995588e545001"
#            for i in range(1180)]

# # Directory to save the downloaded .ts files
# download_directory = "downloaded_videos"