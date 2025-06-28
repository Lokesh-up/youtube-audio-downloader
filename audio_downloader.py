import yt_dlp

def download_audio(url):
    options = {
        'format': 'bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',
        'ffmpeg_location': r'C:\Users\vorug\OneDrive\Pictures\Desktop\ffmpeg-7.1.1-essentials_build\ffmpeg-7.1.1-essentials_build\bin',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'noplaylist': True,
    }

    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    video_url = input("Enter YouTube video URL: ")
    download_audio(video_url)
