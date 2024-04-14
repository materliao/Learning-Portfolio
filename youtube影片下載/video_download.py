from pytube import YouTube
import os

def find_videos_folder():
    for root, dirs, files in os.walk(os.getcwd()):
        if 'videos' in dirs:
            return os.path.join(root, 'videos')
    videos_folder = os.path.join(os.getcwd(), 'videos')
    os.makedirs(videos_folder)
    return videos_folder

def download_video():
    videos_folder = find_videos_folder()
    youtubeObject = YouTube(input("Link:"))
    streams = youtubeObject.streams
    highest_resolution_stream = streams.get_highest_resolution()
    highest_resolution_stream.download(videos_folder)
    title = youtubeObject.title
    print("Video:", title, "is downloaded to:", videos_folder)

if __name__ == "__main__":
    download_video()
