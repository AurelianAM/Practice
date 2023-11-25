from video import Video
class Course():

    def __init__(self, id,name=None):
        self.id = f"{id:03d}"
        self.name = name
        self.videos = []
    
    def addVideo(self, id, url):
        newVideo = Video(id, url)
        self.videos.append(newVideo)
    
    def listVideos(self):
        for video in self.videos:
            print(f"{video.id} {video.file_name} {video.maxFiles}")


if __name__ == "__main__":
    c1 = Course(1, "Blockchain_Technologies")

    c1.addVideo(1, "https://5a6b2f0cf3969.streamlock.net:4443/vod/_definst_/2023/20230719173000ROC2_RO/20230719173000ROC2_RO_aac.mp4/media_w915551497_1261.ts?hash=d6203e2335628539dfd789f51aa7a65f431161cd")

    c1.listVideos()
