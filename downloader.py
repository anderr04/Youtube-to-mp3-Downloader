import os
import sys

# Install yt-dlp automatically if it is not installed
try:
    import yt_dlp
except ImportError:
    print("yt-dlp is not installed. Installing it automatically...")
    os.system(f'"{sys.executable}" -m pip install yt-dlp')
    import yt_dlp

def download_songs(text_file):
    if not os.path.exists(text_file):
        print(f"❌ Could not find file '{text_file}'.")
        print("Creating an example file...")
        with open(text_file, "w", encoding="utf-8") as f:
            f.write("Queen - Bohemian Rhapsody\n")
            f.write("Daft Punk - Get Lucky\n")
        print(f"¡File '{text_file}' created! Add your song names to it and run the program again.")
        return

    with open(text_file, "r", encoding="utf-8") as f:
        # Filter empty lines
        songs = [line.strip() for line in f if line.strip()]

    if not songs:
        print(f"⚠️ The file {text_file} is empty. Add the title of some songs.")
        return

    print(f"🎵 Found {len(songs)} songs or links to download.")

    output_folder = "Downloads"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Base yt-dlp options for downloading mp3 format
    base_options = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320', # Maximum quality possible for MP3
        }],
        'outtmpl': f'{output_folder}/%(title)s.%(ext)s', # Save in Downloads folder
        'quiet': False,
    }

    for i, song in enumerate(songs, 1):
        is_url = song.startswith("http://") or song.startswith("https://")
        
        # Copy base options to configure them based on URL vs search
        options = dict(base_options)
        
        if is_url:
            search_query = song
            print(f"\n==================================================")
            print(f"[{i}/{len(songs)}] Detected URL: {song}")
            
            options['default_search'] = 'auto'
            # Allow playlist downloading if it's a URL containing 'list='
            if "list=" in song:
                options['noplaylist'] = False
                print(f"      (Playlist detected! Downloading all videos...)")
            else:
                options['noplaylist'] = True
            print(f"==================================================")
        else:
            search_query = f"{song} lyrics"
            print(f"\n==================================================")
            print(f"[{i}/{len(songs)}] Searching: {song}")
            print(f"      (Smart search term used: '{search_query}')")
            print(f"==================================================")
            
            options['default_search'] = 'ytsearch1'
            options['noplaylist'] = True

        # Initialize the downloader with the current options
        with yt_dlp.YoutubeDL(options) as ydl:
            try:
                ydl.download([search_query])
                print(f"✅ Download completed!")
            except Exception as e:
                print(f"❌ Error processing '{song}': {e}")
                
    print("\n🎉 All downloads have finished!")

if __name__ == "__main__":
    download_songs("songs.txt")
    print("\nPress ENTER to close the program...")
    input()
