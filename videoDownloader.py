from pytube import YouTube
from sys import argv
import os

desktopPath = os.path.join(os.path.expanduser('~'), 'Desktop')
folderName = "Downloaded_Videos"
folderPath = os.path.join(desktopPath, folderName)
os.makedirs(folderPath, exist_ok=True)
link = argv[1]
videoLink = YouTube(link)

videoDownload = videoLink.streams.get_highest_resolution()

videoDownload.download(folderPath)