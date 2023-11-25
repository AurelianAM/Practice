from download_with_threads import download_videos
from concatenare import concatenare
from compress import compress

TEMP_FOLDER = "downloaded_videos"

start_url = "5a6b2f0cf3969"
site_file = "w928512657"
file_hash = "2aa7f06f38cee006e90a0238b790594ed06d5af5"
segments = 1270

compressed_filename = "Consultatie_Python_and_Programming_Fundamentals"

# url1 = "https://5e6f49934c5f8.streamlock.net:4443/vod/_definst_/2022/20221101173000ROC3_RO/20221101173000ROC3_RO_aac.mp4/media_w188600440_1169.ts?hash=7ce3e674b65c24a34a9e0ed1347995588e545001"
    # 1169
# url2 = "https://5a6b2f0cf3969.streamlock.net:4443/vod/_definst_/2022/20221103173000ROC3_RO/20221103173000ROC3_RO_aac.mp4/media_w755169945_1200.ts?hash=c6b7fcfc2232508bedde1cab26b5c2a4e6f8ef32"
    # 1200
# url3 = "https://5e6f49934c5f8.streamlock.net:4443/vod/_definst_/2022/20221108173000ROC3_RO/20221108173000ROC3_RO_aac.mp4/media_w638427682_1200.ts?hash=d22a43c93628142671aa32808aeb874ee3e7cebb"
    # 1200
# url4 = "https://5aa64ca8b95b8.streamlock.net:4443/vod/_definst_/2022/20221110173000ROC3_RO/20221110173000ROC3_RO_aac.mp4/media_w100099219_1171.ts?hash=1b139efc69497b122374bdf9e3ca651392dd20ec"
    # 1171
# url5 = "https://5a6b2f0cf3969.streamlock.net:4443/vod/_definst_/2022/20221115173000ROC3_RO/20221115173000ROC3_RO_aac.mp4/media_w1706206213_1209.ts?hash=26bdadf55ee4e9dd916b0617dad8635b3ad447f2"
    # 1209
# url6 = "https://5e6f49934c5f8.streamlock.net:4443/vod/_definst_/2022/20221117173000ROC3_RO/20221117173000ROC3_RO_aac.mp4/media_w95100271_1191.ts?hash=793123aebdbcca7382a83576e0c4cec717461c11"
    # 1191
# url7 = "https://5e6f49934c5f8.streamlock.net:4443/vod/_definst_/2022/20221122173000ROC3_RO/20221122173000ROC3_RO_aac.mp4/media_w515932731_1207.ts?hash=30f8041f50eb36ce2133562273ca89d10562cbb5"
    # 1207
# url8 = "https://5aa64ca8b95b8.streamlock.net:4443/vod/_definst_/2022/20221124173000ROC3_RO/20221124173000ROC3_RO_aac.mp4/media_w1634914331_1178.ts?hash=2b8f5abb0b860e8addaf9f1b906bc72cb30546b2"
    # 1178
# url_cons = "https://5a6b2f0cf3969.streamlock.net:4443/vod/_definst_/2022/20221121173000ROC1_RO/20221121173000ROC1_RO_aac.mp4/media_w928512657_1270.ts?hash=2aa7f06f38cee006e90a0238b790594ed06d5af5"
    # 1270

# urli = ""
    # 

# urli = ""
    # 

urlList = [f"https://{start_url}.streamlock.net:4443/vod/_definst_/2022/20221103173000ROC3_RO/20221103173000ROC3_RO_aac.mp4/media_{site_file}_{i}.ts?hash={file_hash}" for i in range(segments)]

download_videos(urlList, TEMP_FOLDER)

concatenare(TEMP_FOLDER)

compress(compressed_filename)

print("Program sucessfully finished... ")