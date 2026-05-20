import spotipy 
import os
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

load_dotenv()

spot_client_id = os.getenv("SPOTIFY_CLIENT_ID")
spot_client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
spot_redirect_uri = "http://127.0.0.1:8888/callback"
spot_scope = "user-library-read"
spot_songs = []

#authentication step
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=spot_client_id, 
                                               client_secret=spot_client_secret, 
                                               redirect_uri=spot_redirect_uri, 
                                               scope=spot_scope))

#read in all liked songs
offset = 0
while True:
    song_batch = sp.current_user_saved_tracks(limit=50, offset=offset)
    songs = []
    
    for item in song_batch["items"]:
        songs.append(item["track"]["name"])
    
    offset += len(songs)
    spot_songs.extend(songs)
    
    if len(songs) != 50:
        break

#print out the songs' name and number it
for num, song in enumerate(spot_songs):
    print(f"{num+1}: {song}")

    





