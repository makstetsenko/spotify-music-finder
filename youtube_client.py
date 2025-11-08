import yt_dlp
import os

# Search options (fetch metadata only)
ydl_opts_extract = {
    "quiet": True,
    "extract_flat": True,
    "default_search": "ytsearch",
}

def get_youtube_download_options_json(download_path):
    return {
        "quiet": True,
        "format": "bestaudio/best",
        "outtmpl": download_path,
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
    }


def search_and_download_mp3(search_text: str, track_duration, duration_threhold=5, download_directory="./downloads"):    
    max_duration = track_duration + duration_threhold
    min_duration = track_duration - duration_threhold

    with yt_dlp.YoutubeDL(ydl_opts_extract) as ydl:
        search_results = ydl.extract_info(f"ytsearch{15}:{search_text}", download=False)

    # Filter by duration
    for entry in search_results["entries"]:
        video_url = entry["url"]
        video_duration = entry["duration"]

        if video_duration >= min_duration and video_duration <= max_duration:
            os.makedirs(download_directory.rstrip("/"), exist_ok=True)
            
            download_options = get_youtube_download_options_json(
                download_path=download_directory.rstrip("/") + "/%(title)s.%(ext)s"
            )
            
            with yt_dlp.YoutubeDL(download_options) as ydl:
                ydl.download([video_url])
            
        
            break
        
    else:
        print("No matching video found within duration limit.")
