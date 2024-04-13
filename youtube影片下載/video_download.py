# coding: utf-8
from pytube import YouTube
import os,time

def find_videos_folder():
    for root, dirs, files in os.walk(os.getcwd()):
        if 'videos' in dirs:
            return os.path.join(root, 'videos')
    return None

def download_video():
    videos_folder = find_videos_folder()
    youtubeObject = YouTube(input("Link:"))
    streams = youtubeObject.streams
    highest_resolution_stream = streams.get_highest_resolution()
    highest_resolution_stream.download(videos_folder)
    title = youtubeObject.title
    print("Video:",title,"is_download_to:", videos_folder)

if __name__ == "__main__":
    download_video()   