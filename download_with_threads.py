# """
# # Concatenare file:
# ulimit -n 2048
# ffmpeg -i "concat:$(printf '%s|' *.ts)" -c copy -bsf:a aac_adtstoasc output.mp4

# # Comprimare:
# ffmpeg -i output.mp4 -c:v h264_nvenc -b:v 1000k -c:a aac -strict experimental compressed_output.mp4

# """


import requests
import os
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
    
    print("Download finished...")


if __name__ == "__main__":
    download_directory = "downloaded_videos"
    # output_filename = "output.avi"

    start_url = "5aa64ca8b95b8"
    site_file = "w100099219"
    file_hash = "1b139efc69497b122374bdf9e3ca651392dd20ec"
    segments = 1171
    # urlList = [f"https://5e6f49934c5f8.streamlock.net:4443/vod/_definst_/2022/20221101173000ROC3_RO/20221101173000ROC3_RO_aac.mp4/media_w188600440_{i}.ts?hash=7ce3e674b65c24a34a9e0ed1347995588e545001"
    #            for i in range(1180)]

    urlList = [f"https://5a6b2f0cf3969.streamlock.net:4443/vod/_definst_/2022/20221103173000ROC3_RO/20221103173000ROC3_RO_aac.mp4/media_w755169945_{i}.ts?hash=c6b7fcfc2232508bedde1cab26b5c2a4e6f8ef32" for i in range(segments)]

    
    download_videos(urlList, download_directory)
        
    print("Download finished...")
