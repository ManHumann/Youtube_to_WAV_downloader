# YouTube WAV Downloader

This project downloads audio from YouTube links and converts it into **WAV format** using `yt-dlp` and `ffmpeg`. The YouTube links are read from a CSV file.

---

## 1. How to Run (User Guide)

### Prerequisites

* Python **3.8+** installed

> **Note:** No manual FFmpeg installation is required if `yt-dlp` can access a system-provided FFmpeg. `yt-dlp` internally uses FFmpeg for audio conversion.

```bash
   pip install -r requirements.txt
```

3. Ensure `ffmpeg` is installed:

   ```bash
   ffmpeg -version
   ```

### Prepare the CSV File

Create a file named **`url.csv`** in the project directory.

Add **one YouTube URL per line**, for example:

```csv
https://www.youtube.com/watch?v=dQw4w9WgXcQ
https://youtu.be/9bZkp7q19f0
```

### Run the Program

```bash
python main.py
```

### Output

* Downloaded audio files will be saved as **`.wav`** files
* Output directory: `downloads/`

---

## 2. How It Works (Technical Overview)

1. The program reads YouTube URLs from `url.csv` using Python’s built-in `csv` module.

2. All valid URLs are collected into a list and passed to `yt-dlp`.

3. `yt-dlp` downloads the **best available audio stream** from each YouTube URL.

4. After downloading, `yt-dlp` automatically invokes **FFmpeg** to:

   * Extract the audio
   * Convert it to **WAV format**
   * Preserve the highest possible audio quality

5. Files are named using the YouTube video title and stored in the `downloads/` folder.

6. If a URL is a playlist, `yt-dlp` automatically downloads and processes all videos in the playlist.

---

## Notes

* `yt-dlp` internally relies on **FFmpeg** for audio extraction and conversion.
* You do **not** import or call FFmpeg directly in the code.
* As long as `yt-dlp` is able to access FFmpeg on your system, WAV conversion will work.
* Only download content you own or have permission to download.

---

## Dependencies

### Python

* `yt-dlp`

### System (Used Internally)

* FFmpeg (used internally by `yt-dlp` for audio conversion)

---

This project is intended for educational and personal use.
