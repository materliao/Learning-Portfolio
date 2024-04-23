# coding: utf-8
from pytube import YouTube
import os

forlder_name = 'musics'

def find_musics_folder():
    for root, dirs, files in os.walk(os.getcwd()):
        if forlder_name in dirs:
            return os.path.join(root, forlder_name)
    musics_folder = os.path.join(os.getcwd(), forlder_name)
    os.makedirs(musics_folder)
    return musics_folder

def download_musics():
    musics_folder = find_musics_folder()
    youtubeObject = YouTube(input("Link:"))
    streams = youtubeObject.streams
    title = youtubeObject.title
    destination = os.path.join(musics_folder, f"{title}.mp3")
    if not os.path.exists(destination):
        youtubeObject.streams.filter().get_audio_only().download(musics_folder)
        print("Music:", title, "is downloaded to:", destination)
    else:
        print("Music already exists in:", destination)

if __name__ == "__main__":
    download_musics()