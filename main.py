import csv
import yt_dlp
from pathlib import Path

def read_csv(csv_file):
    urls = []
    with open(csv_file, mode='r',newline="",encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[0].strip():
                urls.append(row[0].strip())
    return urls

def download_youtube_wav(urls, output_dir="downloads"):
    Path(output_dir).mkdir(exist_ok=True)

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": f"{output_dir}/%(title)s.%(ext)s",
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "wav",
                "preferredquality": "0",
            }
        ],
        "quiet": False,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download(urls)

if __name__ == "__main__":
    csv_file = "url.csv"

    urls = read_csv(csv_file)

    if not urls:
        print("No URLs found in url.csv")
    else:
        download_youtube_wav(urls)