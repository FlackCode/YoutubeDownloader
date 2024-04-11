from pytube import YouTube
from getch import pause
import os

desktopPath = os.path.join(os.path.expanduser('~'), 'Desktop')
folderName = "Downloaded Videos"
folderPath = os.path.join(desktopPath, folderName)
os.makedirs(folderPath, exist_ok=True)

print('Welcome to Youtube Downloader!')
link = input('Enter your youtube video link to download it: ')
ytLink = str(link)
videoLink = YouTube(ytLink)
print(f"Downloading \"{videoLink.title}\" to desktop!")
videoDownload = videoLink.streams.get_highest_resolution()
videoDownload.download(folderPath)
print("Video successfully downloaded!")
pause("Press Any Key To Exit.")