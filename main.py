import tkinter as tk
import customtkinter
from downloader import Downloader

# System Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

def create_link_list():
    text = link.get("0.0", "end")
    linkList = text.splitlines()
    print(linkList)

    for url in linkList:
        Downloader.downloadMP3(url);

if __name__ == '__main__':
    
    # App Frame
    app = customtkinter.CTk()
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
    
    app.mainloop()