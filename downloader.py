import os
import sys

try:
    import yt_dlp
except ImportError:
    os.system(f'"{sys.executable}" -m pip install yt-dlp')
    import yt_dlp

SONGS_FILE = "songs.txt"
OUTPUT_FOLDER = "Downloads"

BASE_OPTIONS = {
    'format': 'bestaudio/best',
    'postprocessors': [
        {'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3',
            'preferredquality': '320'},
        {'key': 'EmbedThumbnail'},
    ],
    'outtmpl': f'{OUTPUT_FOLDER}/%(title)s.%(ext)s',
    'writethumbnail': True,
    'quiet': False,
}


def load_songs(path):
    if not os.path.exists(path):
        with open(path, "w", encoding="utf-8") as f:
            f.write("Queen - Bohemian Rhapsody\nDaft Punk - Get Lucky\n")
        print(f"'{path}' not found -- created with examples. Edit it and re-run.")
        return []

    songs = [l.strip() for l in open(path, encoding="utf-8") if l.strip()]
    if not songs:
        print(f"'{path}' is empty. Add some song names or URLs.")
    return songs


def build_options(song):
    is_url = song.startswith("http://") or song.startswith("https://")
    opts = {
        **BASE_OPTIONS,
        'default_search': 'auto' if is_url else 'ytsearch1',
        'noplaylist': not (is_url and "list=" in song),
    }
    query = song if is_url else f"{song} lyrics"
    return opts, query


def download_songs(path):
    songs = load_songs(path)
    if not songs:
        return

    os.makedirs(OUTPUT_FOLDER, exist_ok=True)
    print(f"{len(songs)} song(s) to download.")

    for i, song in enumerate(songs, 1):
        opts, query = build_options(song)
        print(
            f"\n[{i}/{len(songs)}] {'URL' if query == song else 'Search'}: {song}")
        with yt_dlp.YoutubeDL(opts) as ydl:
            try:
                ydl.download([query])
                print("Done.")
            except Exception as e:
                print(f"Error: {e}")

    print("\nAll downloads finished.")
    open(path, 'w').close()


if __name__ == "__main__":
    download_songs(SONGS_FILE)
    input("\nPress ENTER to close...")
