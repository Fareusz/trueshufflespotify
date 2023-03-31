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
print(Fore.RED + "Script will now fetch all songs from your liked songs... this may take a while")



def playrandom(tracks):
    random_track = random.choice(tracks)
    track_uri = random_track["track"]["uri"]

    sp.start_playback(uris=[track_uri])

    print(Fore.GREEN + "Playing: " + random_track['track']['name'] + " by " + random_track['track']['artists'][0]['name'])

def is_track_playing():
    current_playback = sp.current_playback()
    return current_playback and current_playback["is_playing"]

def get_all_saved_tracks():
    all_tracks = []
    limit = 50
    offset = 0

    while True:
        print(Fore.BLUE + 'Getting tracks {} to {}'.format(offset, offset + limit - 1))
        results = sp.current_user_saved_tracks(limit=limit, offset=offset)
        tracks = results["items"]

        if not tracks:
            break

        all_tracks.extend(tracks)
        offset += limit

    return all_tracks

all_tracks = get_all_saved_tracks()
playrandom(all_tracks)

while True:
    time.sleep(1)
    if not is_track_playing():
        random.seed(random.randint(0, 1000000))
        playrandom(all_tracks)