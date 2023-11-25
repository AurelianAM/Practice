from urllib.parse import urlparse, parse_qs

url = "https://5a6b2f0cf3969.streamlock.net:4443/vod/_definst_/2023/20230719173000ROC2_RO/20230719173000ROC2_RO_aac.mp4/media_w915551497_1261.ts?hash=d6203e2335628539dfd789f51aa7a65f431161cd"

# Parse the URL
parsed_url = urlparse(url)

# Extract components
scheme = parsed_url.scheme
host = parsed_url.netloc
path = parsed_url.path
query = parsed_url.query

# Extract path segments
path_segments = path.split('/')

# Extract query parameters
query_params = parse_qs(query)

# Print the components
print(f"Scheme: {scheme}")
print(f"Host: {host}")

print("Path Segments:")
for segment in path_segments:
    print(segment)

# Print query parameters
print("Query Parameters:")
for key, values in query_params.items():
    print(f"{key}: {', '.join(values)}")

# file_name = path_segments[-1]
# length = int((file_name.split("_")[-1]).split(".")[0])
# print(f"File Name: {file_name}")
# print(f"Length: {length}")

print("Segmentele adunate")
print("/".join(path_segments[0:len(path_segments) - 1]))