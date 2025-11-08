# spotify-music-finder

Downloads music from spotify URL with yt-dlp.

Flow:

1) Get track's details from Sporify (name, artist, duration)
2) Find track on Youtube with these params (name, artist, duration)
3) If found then download as mp3

This app can download by:

1) Track URL
2) Playlist URL

All download tracks go to `./downlods` directory.
If downloading playlits then download directory is `./downlods/PLAYLIST-NAME`.

## Usage

1) You need to create `SPOTIPY_CLIENT_ID` and `SPOTIPY_CLIENT_SECRET` under your Spotify account
2) Add secrets to `.env` file (Check `.env.example` for reference).
3) Create venv: `python -m venv venv`
4) Use venv: `source venv/bin/activate`
5) Install requirements:  `python -m pip install -r requirements.txt`
6) Run: `python main.py "LINK TO TRACK OR PLAYLIST"`. 

For example:

1) `python main.py https://open.spotify.com/playlist/5qo84PZdJJ2j0brFZCDbxs`
2) `python main.py https://open.spotify.com/track/08njDfgJSE2K4tz218WvnY`
