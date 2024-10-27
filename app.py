import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Replace with your Spotify Developer credentials
CLIENT_ID = 'UR ID'
CLIENT_SECRET = 'UR Secret'
REDIRECT_URI = 'http://localhost:8888/callback'

# Set the scope to read your liked songs
SCOPE = 'user-library-read'

# Authenticate with Spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope=SCOPE))

# Retrieve all liked songs
def get_all_liked_songs():
    songs = []
    offset = 0
    limit = 50  # Set to 50 to fetch more songs per request
    
    while True:
        # Fetch a page of liked songs
        results = sp.current_user_saved_tracks(limit=limit, offset=offset)
        if not results['items']:
            break  # Exit the loop if there are no more items
        
        # Extract relevant information
        for item in results['items']:
            track = item['track']
            song_info = {
                'name': track['name'],
                'artist': track['artists'][0]['name'],
                'album': track['album']['name'],
                'release_date': track['album']['release_date']
            }
            songs.append(song_info)
        
        # Move to the next page
        offset += limit
    
    return songs

# Fetch all liked songs and export them to a text file
liked_songs = get_all_liked_songs()
txt_filename = 'songs.txt'

with open(txt_filename, 'w', encoding='utf-8') as file:
    for idx, song in enumerate(liked_songs, start=1):
        file.write(f"{song['name']} - {song['artist']}\n")

print(f"Your liked songs have been saved to {txt_filename}")
