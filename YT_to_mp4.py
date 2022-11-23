# YT_to_mp4.py

from pytube import YouTube

link = input("Enter video link:")
video = YouTube(link).streams.filter(file_extension="mp4").first()
video.download()
