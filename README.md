# README for YouTube and Spotify Audio Downloader

## Overview

This project consists of two Python scripts: one that downloads audio from YouTube and converts it to MP3 format, and another that retrieves your liked songs from Spotify and saves them to a text file. After exporting the songs to a text file, the first script can be used to download those songs from YouTube based on the saved information.

## Prerequisites

Before running these scripts, ensure you have Python installed on your system. It's recommended to use Python 3.7 or later.

### Required Libraries

You need to install the following Python libraries:

- `yt-dlp` for downloading audio from YouTube.
- `pydub` for audio conversion.
- `spotipy` for interacting with the Spotify API.

You can install these libraries using pip:

```bash
pip install yt-dlp pydub spotipy
```

### Additional Requirements

- **FFmpeg**: This is required by `pydub` for handling audio conversions. You need to have FFmpeg installed on your system. You can download it from [FFmpeg's official website](https://ffmpeg.org/download.html). Follow the installation instructions for your operating system.

## Setting Up

### Spotify API Credentials

To fetch your liked songs from Spotify, you need to set up a Spotify Developer account and create an application to obtain your `CLIENT_ID`, `CLIENT_SECRET`, and `REDIRECT_URI`. Here are the steps:

1. Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications).
2. Create a new application.
3. Copy the `CLIENT_ID` and `CLIENT_SECRET` provided.
4. Set the Redirect URI to `http://localhost:8888/callback`.
5. Add the required scopes (`user-library-read`) for reading your saved tracks.

Update the following constants in the script with your credentials:

```python
CLIENT_ID = 'your_client_id_here'
CLIENT_SECRET = 'your_client_secret_here'
REDIRECT_URI = 'http://localhost:8888/callback'
```

## How to Use

### Step 1: Retrieve Liked Songs from Spotify

Run the following script to fetch your liked songs from Spotify and save them to a text file named `songs.txt`.

```python
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Your Spotify API credentials go here
CLIENT_ID = 'your_client_id_here'
CLIENT_SECRET = 'your_client_secret_here'
REDIRECT_URI = 'http://localhost:8888/callback'
SCOPE = 'user-library-read'

# Authenticate with Spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope=SCOPE))

# Retrieve all liked songs
def get_all_liked_songs():
    # Code to fetch liked songs goes here...

# Fetch all liked songs and export them to a text file
liked_songs = get_all_liked_songs()
txt_filename = 'songs.txt'

with open(txt_filename, 'w', encoding='utf-8') as file:
    for idx, song in enumerate(liked_songs, start=1):
        file.write(f"{song['name']} - {song['artist']}\n")
```

After running the script, your liked songs will be saved in `songs.txt`.

### Step 2: Download Songs from YouTube

Now you can use the second script to download these songs from YouTube and convert them to MP3 format. Ensure the `songs.txt` file is in the same directory as this script.

```python
import yt_dlp
from pydub import AudioSegment
import os

def download_and_convert_to_mp3(query, title):
    # Code to download and convert songs goes here...

def main():
    with open("songs.txt", "r", encoding="utf-8") as file:
        songs = [line.strip() for line in file if line.strip()]

    for song in songs:
        title = song
        download_and_convert_to_mp3(song, title)

if __name__ == "__main__":
    main()
```

### Running the Script

Simply execute the script in your terminal:

```bash
python download_and_convert.py
```

This will download each song listed in `songs.txt`, convert them to MP3, and save them in the `downloads` folder.

## Important Notes

- Make sure you have a stable internet connection while downloading.
- You may need to manually authenticate and provide permission the first time you access your Spotify data.
- The downloaded MP3 files will be saved in a folder named `downloads` in the same directory as the script.

## Troubleshooting

- If you encounter any issues, make sure that your Python environment is set up correctly and all required libraries are installed.
- Check your FFmpeg installation and ensure it's added to your system's PATH.

## License

This project is open-source and available for personal use. Ensure compliance with YouTube and Spotify's terms of service when using this tool.
﻿# Spotify-song-exporter
