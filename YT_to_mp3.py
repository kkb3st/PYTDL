# YT_to_mp3.py

import os
from pytube import YouTube
import subprocess


link = input("Enter video link:")

video = YouTube(link).streams.filter(only_audio=True).first()
out_file = video.download()
new_file = out_file[:-4] + ".mp3"
subprocess.call(['ffmpeg', '-i', out_file, new_file])
os.remove(out_file)
