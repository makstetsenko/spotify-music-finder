from spotify_client import get_track_details, get_playlist, is_track, is_playlist
from youtube_client import search_and_download_mp3
import sys


def download_track(url):
    track_details = get_track_details(url)

    print("Track:", track_details.name)
    search_and_download_mp3(search_text=track_details.name, track_duration=track_details.duration)
    
    
def download_playlist(url):
    playlist = get_playlist(url)
    
    print("Playlist:", playlist.name)
    print("Tracks:", len(playlist.tracks))
    
    for t in playlist.tracks:
        print("Track:", t.name)
        
        try:
            search_and_download_mp3(
                search_text=t.name, 
                track_duration=t.duration,
                download_directory="./downloads/" + playlist.name)
        except KeyboardInterrupt:
            print("Download was cancelled")
            break
        except:
            print("Download failed")
    
    
def main(): 
    url = sys.argv[1]

    if is_track(url):
        download_track(url)
        
    if is_playlist(url):
        download_playlist(url)
        
        

try:
    main()
except KeyboardInterrupt:
    print("Download was canceled")