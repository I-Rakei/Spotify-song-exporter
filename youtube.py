import yt_dlp
from pydub import AudioSegment
import os

def download_and_convert_to_mp3(query, title):
    download_path = "./downloads"
    os.makedirs(download_path, exist_ok=True)
    
    # Temporary path for the downloaded file
    temp_audio_path = os.path.join(download_path, f"{title}.webm")

    # Set up yt-dlp options for downloading audio only
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': temp_audio_path,
        'quiet': True,
        'noplaylist': True,
    }

    try:
        # Download audio from YouTube
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Downloading: {title}")
            ydl.download([f"ytsearch:{query}"])

        # Convert to MP3 using pydub
        mp3_path = os.path.join(download_path, f"{title}.mp3")
        audio = AudioSegment.from_file(temp_audio_path)
        audio.export(mp3_path, format="mp3")
        
        # Remove the temporary file
        os.remove(temp_audio_path)
        print(f"Downloaded and converted to MP3: {title}")
    
    except Exception as e:
        print(f"Error downloading {title}: {e}")

def main():
    # Specify UTF-8 encoding to handle special characters
    with open("songs.txt", "r", encoding="utf-8") as file:
        songs = [line.strip() for line in file if line.strip()]

    for song in songs:
        title = song  # Use the line as title for naming the file
        download_and_convert_to_mp3(song, title)

if __name__ == "__main__":
    main()