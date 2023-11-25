import re
from urllib.parse import urlparse, parse_qs

def extract_info_from_url(url):
    """Extract info from a URL from LinkAcademy
    
    Parameters
    ----------
    url : str
        The URL to extract info from
    
    Returns
    -------
    filename : str
        The filename of the video
    base_file : str
        The base file of the video
    length : str
        The length of the video
    url_prefix : str
        The URL prefix of the video
    hash_param : str
        The hash parameter of the video"""
    # Parse the URL
    parsed_url = urlparse(url)
    
    # Extract the first 13 characters from the URL
    url_prefix = url.split('//')[1][:13]
    
    # Extract the filename from the path
    filename = parsed_url.path.split('/')[-1]
    
    # Extract the base_file from the filename
    base_file_match = re.search(r'^media_w(\d+)_', filename)
    base_file = None
    if base_file_match:
        base_file = f'media_w{base_file_match.group(1)}'
    
    # Extract the length from the last four digits of the filename
    length_match = re.search(r'(\d{4})\.ts', filename)
    length = None
    if length_match:
        length = length_match.group(1)
    
    # Extract the hash parameter
    query_params = parse_qs(parsed_url.query)
    hash_param = query_params.get('hash', [None])[0]
    
    return filename, base_file, length, url_prefix, hash_param

if __name__ == "__main__":
        
    # Define the list of URLs
    urls = [
        "https://5e6f49934c5f8.streamlock.net:4443/vod/_definst_/2022/20221101173000ROC3_RO/20221101173000ROC3_RO_aac.mp4/media_w188600440_1169.ts?hash=7ce3e674b65c24a34a9e0ed1347995588e545001", 
        "https://5a6b2f0cf3969.streamlock.net:4443/vod/_definst_/2022/20221103173000ROC3_RO/20221103173000ROC3_RO_aac.mp4/media_w755169945_1200.ts?hash=c6b7fcfc2232508bedde1cab26b5c2a4e6f8ef32", 
        "https://5e6f49934c5f8.streamlock.net:4443/vod/_definst_/2022/20221108173000ROC3_RO/20221108173000ROC3_RO_aac.mp4/media_w638427682_1200.ts?hash=d22a43c93628142671aa32808aeb874ee3e7cebb", 
        "https://5aa64ca8b95b8.streamlock.net:4443/vod/_definst_/2022/20221110173000ROC3_RO/20221110173000ROC3_RO_aac.mp4/media_w100099219_1171.ts?hash=1b139efc69497b122374bdf9e3ca651392dd20ec", 
        "https://5a6b2f0cf3969.streamlock.net:4443/vod/_definst_/2022/20221115173000ROC3_RO/20221115173000ROC3_RO_aac.mp4/media_w1706206213_1209.ts?hash=26bdadf55ee4e9dd916b0617dad8635b3ad447f2", 
        "https://5e6f49934c5f8.streamlock.net:4443/vod/_definst_/2022/20221117173000ROC3_RO/20221117173000ROC3_RO_aac.mp4/media_w95100271_1191.ts?hash=793123aebdbcca7382a83576e0c4cec717461c11", 
        "https://5e6f49934c5f8.streamlock.net:4443/vod/_definst_/2022/20221122173000ROC3_RO/20221122173000ROC3_RO_aac.mp4/media_w515932731_1207.ts?hash=30f8041f50eb36ce2133562273ca89d10562cbb5", 
        "https://5aa64ca8b95b8.streamlock.net:4443/vod/_definst_/2022/20221124173000ROC3_RO/20221124173000ROC3_RO_aac.mp4/media_w1634914331_1178.ts?hash=2b8f5abb0b860e8addaf9f1b906bc72cb30546b2"
    ]

    # Process and print information for each URL
    for url in urls:
        filename, base_file, length, url_prefix, hash_param = extract_info_from_url(url)
        print(f"URL: {url}")
        print(f"Filename: {filename}")
        print(f"Base File: {base_file}")
        print(f"Length: {length}")
        print(f"URL Prefix: {url_prefix}")
        print(f"Hash Parameter: {hash_param}")
        print()
