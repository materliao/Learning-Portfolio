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
    title = youtubeObject.title
    destination = os.path.join(videos_folder, f"{title}.mp4")
    if not os.path.exists(destination):
        highest_resolution_stream.download(videos_folder)
        print("Video:", title, "is downloaded to:", destination)
    else:
        print("Video already exists in:", destination)

if __name__ == "__main__":
    download_video()
