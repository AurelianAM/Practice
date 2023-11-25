import tkinter as tk
from tkinter import ttk
from video import Video
import threading

def download_video():
    link = entry_link.get()
    output_filename = entry_filename.get()
    conc = concatenate.get()
    comp = compress.get()

    video = Video(1, link, output_filename)
    video.getVideoFile(concatenate=conc, compress=comp)

    # Start the download process in a separate thread to avoid blocking the GUI
    def download_video_thread():
        # Update the progress bar as the download progresses
        if comp:
            while not video.isDownloadComplete():
                progress_bar['value'] = video.getDownloadProgress() * 100
                root.update()


    thread = threading.Thread(target=download_video_thread)
    thread.start()


root = tk.Tk()

label_link = tk.Label(root, text="Video Link:")
label_link.pack()
entry_link = tk.Entry(root)
entry_link.pack()

label_filename = tk.Label(root, text="Output Filename:")
label_filename.pack()
entry_filename = tk.Entry(root)
entry_filename.pack()

concatenate = tk.BooleanVar()
compress = tk.BooleanVar()

checkbox_concatenate = tk.Checkbutton(root, variable=concatenate, text="Concatenate", onvalue=True, offvalue=False)
checkbox_concatenate.pack()

checkbox_compress = tk.Checkbutton(root, variable=compress, text="Compress", onvalue=True, offvalue=False)
checkbox_compress.pack()

# Create a progress bar window
progress_bar = ttk.Progressbar(root, orient=tk.HORIZONTAL, mode='indeterminate')
progress_bar.pack(pady=10)

button_download = tk.Button(root, text="Download Video", command=download_video)
button_download.pack()

root.mainloop()


"""
WebAppBuild_6
https://5a6b2f0cf3969.streamlock.net:4443/vod/_definst_/2023/20230406173000ROC3_RO/20230406173000ROC3_RO_aac.mp4/media_w1567744851_1151.ts?hash=bc18e6fdc3c51b3ce2612f7a7487312122d3ce30

WebAppBuild_5
https://5a6b2f0cf3969.streamlock.net:4443/vod/_definst_/2023/20230330173000ROC3_RO/20230330173000ROC3_RO_aac.mp4/media_w1501314858_1194.ts?hash=87a89b0987cb8da28f5ededbadac87daebe994b4
"""