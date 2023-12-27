from pytube import YouTube
from moviepy.editor import *
import string
import os

class Downloader:
    def downloadMP3(url: string, dest: string) -> string:
        try:
            ytObject = YouTube(url)
            audio = ytObject.streams.get_highest_resolution()
            audio.download(output_path=dest)

            print("Download successfull | url: " + url)  
            return audio.default_filename
        except:
            print("Download failed | url: " + url)      

    def convertToMP3(mp4, mp3):
        FILETOCONVERT = AudioFileClip(mp4)
        FILETOCONVERT.write_audiofile(mp3)
        FILETOCONVERT.close()