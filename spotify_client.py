import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv

class TrackDetails:
    def __init__(self, name = None, duration = None, spotify_track = None):
        if spotify_track is not None:
            
            artist_names = []
            song_name = spotify_track["name"]

            for a in spotify_track["artists"]:
                artist_names.append(a["name"])
                
            
            self.name = " ".join(artist_names) + " - " + song_name
            self.duration = int(spotify_track["duration_ms"] / 1000)
            
            return
        
        self.name = name
        self.duration = duration
        
    
class PlaylistDetails:
    def __init__(self, name: str, tracks: list[TrackDetails]):
        self.name = name
        self.tracks = tracks
    


load_dotenv()


auth_manager = SpotifyClientCredentials()
spotify_client = spotipy.Spotify(auth_manager=auth_manager)


def get_track_details(url: str) -> TrackDetails:
    track = spotify_client.track(url)
    return TrackDetails(spotify_track=track)


def get_playlist(url: str) -> PlaylistDetails:
    tracks: list[TrackDetails] = []
    page_size = 100
    offset = 0
    
    while 1:
        tracks_response = spotify_client.playlist_tracks(url, offset=offset, limit=page_size)
        
        for track_item in tracks_response["items"]:            
            tracks.append(TrackDetails(spotify_track=track_item["track"]))
        
        if tracks_response["next"] is None:
            break
        
        offset += page_size
        
    playlist_response = spotify_client.playlist(url)
    
    return PlaylistDetails(
        name=playlist_response["name"],
        tracks=tracks
    )
        

def is_track(url) -> bool:
    return "/track/" in url


def is_playlist(url) -> bool:
    return "/playlist/" in url