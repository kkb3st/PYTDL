# YT_to_mp3.py

import youtube_dl
video_url = input("Enter video url:")
video_info = youtube_dl.YoutubeDL().extract_info(url=video_url, download=False)
file_name = video_info['title'] + ".mp3"
options = {
    'format': 'bestaudio/best',
    'keepvideo': 'false',
    'outtmpl': file_name,
}
with youtube_dl.YoutubeDL(options) as ydl:
    ydl.download([video_info['webpage_url']])

print("Download complete! {}".format(file_name))
