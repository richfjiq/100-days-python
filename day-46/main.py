import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv

load_dotenv()

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
SPOTIFY_REDIRECT_URI = os.getenv("SPOTIFY_REDIRECT_URI")

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        redirect_uri=SPOTIFY_REDIRECT_URI,
        scope="playlist-modify-private",
    )
)

URL = "https://www.billboard.com/charts/hot-100"

date = input(
    "Which year of the past do you want to travel to? Type the date in this format YYYY-MM-DD:\n"
)
user_id = sp.current_user()["id"]
response = requests.get(url=f"{URL}/{date}")
billboard_page = response.text
soup = BeautifulSoup(billboard_page, "html.parser")
title_songs = soup.select("li ul li h3")
song_uris = []

for title in title_songs:
    track_title = title.getText()
    sp_search = sp.search(q=f"{track_title.strip()}", type="track")
    try:
        track_uri = sp_search["tracks"]["items"][0]["uri"]
        song_uris.append(track_uri)
    except:
        print(f"{track_title} doesn't exist in Spotify. Skipped.")


playlist = sp.user_playlist_create(
    user=user_id,
    name=f"{date} Billboard 100",
    public=False,
    collaborative=False,
    description=f"{date} Billboard 100",
)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
