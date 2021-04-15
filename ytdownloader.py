import tkinter as tk
from tkinter import ttk
from pytube import YouTube
import os

window = tk.Tk()
window.geometry('500x300')
window.resizable(0, 0)
window.title("youtube downloader")
text1 = tk.Label(text="Youtube downloader", font="arial 20 bold").pack()
text2 = tk.Label(text="insert video url here", font="arial 10").pack()
link = tk.StringVar()
_user_ = tk.Entry(width=50, textvariable=link).pack()


def Downloader_mp4():
    url = YouTube(str(link.get()))
    video = url.streams.first()
    out_file = video.download()


def Downloader_mp3():
    url = YouTube(str(link.get()))
    video = url.streams.first()
    out_file = video.download()
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)

text3 = tk.Label(text='select file format', font="arial 10").pack()
button1 = tk.Button(window, text = 'download mp3', command = Downloader_mp3, bg = "#4958e3", fg = "#ffffff").place(x = 150, y = 120)
button2 = tk.Button(window, text = 'download mp4', command = Downloader_mp4, bg = "red", fg = "#ffffff").place(x = 260, y = 120)
