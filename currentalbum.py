import os
import sys
import json
import spotipy
import webbrowser
import credentials
import time
import spotipy.util as util
from spotipy.oauth2 import SpotifyOAuth
from json.decoder import JSONDecodeError

# Get the username from terminal

username = "jayypeg"
scope = "user-read-private user-read-playback-state user-modify-playback-state playlist-read-private user-read-currently-playing"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=credentials.client_ID, client_secret=credentials.client_SECRET,
                                                   redirect_uri=credentials.redirect_url, scope=scope))
def currentplay():
    # user id: jayypeg


    result = sp.current_user_playing_track()
    # print(json.dumps(result, sort_keys=True, indent=4))

    if result is None:
        print()
        print("No song playing")
    else:
        song = result["item"]["name"]
        imageURL = result["item"]["album"]["images"][0]["url"]
        webbrowser.open(imageURL)


    # get current device
    devices = sp.devices()
    #print(json.dumps(devices, sort_keys=True, indent=4))
    deviceID = devices['devices'][0]['id']

    # current track info
    track = sp.current_user_playing_track()
    # print(json.dumps(track, sort_keys=True, indent=4))
    print()
    if result is not None:
        artist = track['item']['artists'][0]['name']
        tracks = track['item']['name']


        if artist != "":
            print("Currently playing " + artist + " - " + tracks)

    while True:
        newtrack = sp.current_user_playing_track()
        if newtrack is not None:
            newtracks = newtrack['item']['name']
            #print(tracks)
            #print(newtracks)
            newartists = newtrack['item']['artists'][0]['name']
            if newtracks == tracks:
                time.sleep(5)
            else:
                print("Currently playing " + newartists + " - " + newtracks)
                imageURL = newtrack["item"]["album"]["images"][0]["url"]
                webbrowser.open(imageURL)
                tracks = newtracks
                time.sleep(5)

def favalbum():
    context = "spotify:album:1y2AzG31F4CuCKQ1rpIzaI"
    devices = sp.devices()
    deviceID = devices['devices'][0]['id']
    sp.start_playback(deviceID, context, None)



def rhcp():
    context = "spotify:album:53tvjWbVNZKd3CvpENkzOC"
    devices = sp.devices()
    deviceID = devices['devices'][0]['id']
    sp.start_playback(deviceID, context, None)


def pf():
    context = "spotify:album:2WT1pbYjLJciAR26yMebkH"
    devices = sp.devices()
    deviceID = devices['devices'][0]['id']
    sp.start_playback(deviceID, context, None)


while True:

    print()
    print("0 - View Currently Playing")
    print("1 - RHCP")
    print("2 - Pink Floyd")
    print("4 - Exit")
    print()
    choice = input("Your choice: ")

    if choice == "1":
        rhcp()
    elif choice == "2":
        pf()
    elif choice == "0":
        currentplay()
    else:
        break
