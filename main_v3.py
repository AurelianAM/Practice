from download_new import download_videos
from concatenare_new import concatenate_video_files_in_order_by_name_without_processes
# from compress import compress
from parsare_url import extract_info_from_url
import os
import json


def get_url_list(pos):
    if os.path.exists("./data.json"):
        with open("./data.json", "r") as f:
            data = json.load(f)
            for url in data[pos]["urlList"]:
                yield url


def get_course_name(pos):
    if os.path.exists("./data.json"):
        with open("./data.json", "r") as f:
            data = json.load(f)
            return data[pos]["courseName"]


TEMP_FOLDER = "downloaded_videos"
POS = 4


course_name = get_course_name(POS)

mainURLs = get_url_list(POS)

for i, url in enumerate(mainURLs):
    filename, base_file, length, url_prefix, hash_param = extract_info_from_url(url)
    length = int(length)
    # print(f"URL: {url}")
    # print(f"Filename: {filename}")
    # print(f"Base File: {base_file}")
    # print(f"Length: {length}")
    # print(f"URL Prefix: {url_prefix}")
    # print(f"Hash Parameter: {hash_param}")
    print()
    segments_URLs_list = [
        f"https://{url_prefix}.streamlock.net:4443/vod/_definst_/2022/20221103173000ROC3_RO/20221103173000ROC3_RO_aac.mp4/{base_file}_{i}.ts?hash={hash_param}"
        for i in range(length)
    ]

    # print("Start downloading...")
    # download_videos(segments_URLs_list, TEMP_FOLDER)

    print("Concatenating video files...")
    # concatenare(TEMP_FOLDER)

    # print("Compressing video files...")
    # compressed_filename = f"00{POS+1}_{course_name}_0{i+1}"
    # compress(compressed_filename)

print("Program sucessfully finished... ")
