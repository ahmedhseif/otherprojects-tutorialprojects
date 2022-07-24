import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint


# Scraping Billboard 100
date = input('Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ')
URL = f"https://www.billboard.com/charts/hot-100/{date}/"

response = requests.get(URL)
response.raise_for_status()
website_html = response.text
soup = BeautifulSoup(website_html, 'html.parser')
titles = soup.find_all(name="h3", class_="u-letter-spacing-0021")
titles = [title.getText().strip() for title in titles]

song_names = []
for title in titles:
    if title != 'Songwriter(s):' and title != 'Producer(s):' and title != 'Imprint/Promotion Label:':
        song_names.append(title)


# Spotify Authentication
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id="fb1d227003fa40d4a539bdde95df9074",
        client_secret="afeac3e096d5440e858d689bc4b8df2c",
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]



#Searching Spotify for songs by title
song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")

    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

#Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

#Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
