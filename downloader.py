from pytube import YouTube
import string
import os

class Downloader:
    def downloadMP3(url: string):
        try:
            ytObject = YouTube(url)
            audio = ytObject.streams.get_highest_resolution()
            audio.download()


        except:
            print("Download failed | url: " + url)
        print("Download complete | url:" + url)