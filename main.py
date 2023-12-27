import tkinter as tk
import customtkinter
import os
from pytube import YouTube
from moviepy.editor import *
import string

# System Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

destinationPath = os.getcwd() + "\\"
defaultPath = True
print("Destination (DEFAULT): " + destinationPath)

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

def create_link_list():
    text = link.get("0.0", "end")
    linkList = text.splitlines()
    print(linkList)

    fileNameList = []

    for url in linkList:
        fileNameList.append(downloadMP3(url, destinationPath))

    print(fileNameList)

    # Convert files to mp3
    for file in fileNameList:
        file = str(file)
        fileName, ext = file.split(sep=".")

        source = destinationPath + fileName + ".mp4"
        dest = destinationPath + fileName + ".mp3"
        print("Src: " + source + " Dest: " + dest)

        convertToMP3(source, dest)
        os.remove(source)


def open_file_dialog():
    foldername = tk.filedialog.askdirectory() + "/"
    global destinationPath 
    destinationPath = foldername
    global defaultPath
    defaultPath = False
    destLabel.configure(text=destinationPath)
    print("Destination: " + foldername)  # prints the selected folder path

if __name__ == '__main__':
    # App Frame
    app = customtkinter.CTk()
    app.resizable(height=False, width=False)
    app.geometry("720x480")
    app.title("YouTube Downloader")
    
    # Window Elements
    title = customtkinter.CTkLabel(app, text="Links zu YouTube Videos einfügen ...")
    title.pack(padx=10, pady=10)
    
    # Link Input
    link = customtkinter.CTkTextbox(app, width=600, height=160,)
    link.pack()

    # Download Button
    download_button = customtkinter.CTkButton(app, text="Download", command=create_link_list)
    download_button.pack(padx=10, pady=10)    

    destLabel = customtkinter.CTkLabel(app, text=destinationPath)
    destLabel.pack()

    # File Dialog Button
    file_dialog_button = customtkinter.CTkButton(app, text="Zielverzeichnis auswählen", command=open_file_dialog)
    file_dialog_button.pack(padx=10, pady=10)

    # Progress Bar
    stepProgressBar = customtkinter.CTkProgressBar(app, width=400)
    stepProgressBar.set(0)
    stepProgressBar.pack(padx=10, pady=10)
    
    app.mainloop()