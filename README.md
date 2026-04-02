# 🎵 Music Bot (Automatic YouTube to MP3 Downloader)

An automated Python script designed to download songs, entire playlists, and podcasts from YouTube (and other platforms), converting them directly to high-quality MP3 files.

Simply provide a list of titles or URLs, and the bot will magically handle the rest!

## ✨ Key Features
- 🧠 **Smart Search:** If you only know the song name, the bot searches YouTube and intelligently filters the results to grab the "Audio Only" or "Lyrics" version, avoiding the long intros of music videos.
- 🔗 **URL & Playlist Support:** You can paste direct video links or even full Playlist URLs! The bot will detect the playlist and automatically download all of its content.
- ⚙️ **Self-Installing:** No complicated setup process. If you don't have the `yt-dlp` library installed, the script will automatically install its own dependencies upon execution.
- 📁 **Organized:** Automatically creates a `/Downloads` folder and elegantly saves all your finished `.mp3` files there.

## 🚀 How to Use It

### 1. Prerequisites
The only things you need to run this program are:
1. **[Python 3](https://www.python.org/downloads/)** installed on your computer.
2. **[FFmpeg](https://ffmpeg.org/download.html)** available on your system (this is the engine responsible for extracting and converting the audio to MP3 at maximum quality).

### 2. Set up your list
Open the `songs.txt` file (or create it if it doesn't exist) and write one song title or link per line:
```text
Queen - Bohemian Rhapsody
https://www.youtube.com/watch?v=dQw4w9WgXcQ
Eminem - Without Me
https://www.youtube.com/playlist?list=PLej... 
```

### 3. Run it!
**If you are on Windows:**
Simply double-click on `start.bat`.

**If you use the terminal (Linux/Mac/Windows):**
Run the following command:
```bash
python downloader.py
```

## 🛠️ Advanced: Changing the Audio Quality or Format

By default, the script downloads the audio in the highest available source quality and transcodes it to a high-quality `mp3` (320 kbps, which is Extreme Quality). If the audio source is lower, yt-dlp respects the original best quality.

If you want to download the audio in a different format (like `wav`, `m4a`, `flac`), you just need to modify a small part inside the `downloader.py` file!

**How to do it:**
Find the `base_options` dictionary (around line ~35) and change the `preferredcodec`:
```python
    'base_options' = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav', # <-- Change 'mp3' to 'wav', 'flac', 'm4a', etc.
            'preferredquality': '320',
        }],
        # ...
    }
```
*(Note: If you remove that whole `postprocessors` block and change `format` to `bestvideo+bestaudio`, it will download it as an MP4 video instead!)*

---
*Created to avoid repetitive tasks and enjoy your music instantly. Does not promote piracy.*
