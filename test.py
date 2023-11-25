import json
import os

# def get_course_name(pos):
#     if os.path.exists('data.json'):
#         with open("./data.json", "r") as f:
#             data = json.load(f)
#             return data[pos]["courseName"]


# if __name__ == "__main__":
#     print(get_course_name(2))

pos = 2
with open("./data.json", 'r') as f:
    data = json.load(f)
    print(data[pos]["courseName"])