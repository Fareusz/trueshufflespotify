import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
from colorama import init, Fore
import time
import random
import os 

init(autoreset=True)

load_dotenv()
scope = "user-library-read user-modify-playback-state user-read-playback-state"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

print(Fore.GREEN + "Welcome to Spotify Randomizer made by Fareusz#1337")

def playrandom():
    results = sp.current_user_saved_tracks()
    tracks = results['items']


    random_track = random.choice(tracks)
    track_uri = random_track['track']['uri']
    sp.start_playback(uris=[track_uri])

    print(Fore.GREEN + "Playing: " + random_track['track']['name'] + " by " + random_track['track']['artists'][0]['name'])

def is_track_playing():
    current_playback = sp.current_playback()
    return current_playback and current_playback["is_playing"]

playrandom()


while True:
    time.sleep(1)
    if not is_track_playing():
        random.seed(random.randint(0, 1000000))
        playrandom()