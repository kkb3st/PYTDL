from __future__ import unicode_literals
import youtube_dl

video_url = input("Enter video url:")
video_info = youtube_dl.YoutubeDL().extract_info(url=video_url, download=False)
file_name = video_info['title'] + ".mp4"
ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([video_info['webpage_url']])

print("Download complete! {}".format(file_name))
    
