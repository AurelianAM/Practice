import sys
sys.path.append("..")
import parsare_url
import json
import os

def get_url_list(pos):
    if os.path.exists('./data.json'):
        with open("./data.json", "r") as f:
            data = json.load(f)
            for url in data[pos]["urlList"]:
                yield url
def get_course_name(pos):
    if os.path.exists('./data.json'):
        with open("./data.json", "r") as f:
            data = json.load(f)
            return data[pos]["courseName"]

urlList = get_url_list(1)
courseName = get_course_name(1)
print(courseName)
for url in urlList:
    file_name, base_file, length, url_prefix, hash_param  = parsare_url.extract_info_from_url(url)
    print(base_file, length, url_prefix, hash_param)