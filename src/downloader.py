import os
from yt_dlp import YoutubeDL

def download_youtube_video(url, save_path="data"):
    try:
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'writeinfojson': True,
            'writedescription': True,
            'writeautomaticsub': True,
            'writesubtitles': True,
            'subtitleslangs': ['en'],
            'quiet': False,
            'ffmpeg_location': 'C:\\Program Files\\ffmpeg\\ffmpeg-7.1.1-essentials_build\\bin',
            'outtmpl': f'{save_path}/%(id)s/%(id)s.%(ext)s'
        }

        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)

        video_id = info.get("id", "unknown")
        title = info.get("title", "unknown")
        channel = info.get("channel", "unknown")

        video_filename = f"{video_id}.{info.get('ext', 'webm')}"
        video_path = os.path.join(save_path, video_id, video_filename)
        transcript_path = os.path.join(save_path, video_id, f"{video_id}.en.vtt")
        metadata_path = os.path.join(save_path, video_id, f"{video_id}.info.json")
        description_path = os.path.join(save_path, video_id, f"{video_id}.description")

        return {
            "video_id": video_id,
            "title": title,
            "channel": channel,
            "video_path": video_path,
            "transcript_path": transcript_path,
            "metadata_path": metadata_path,
            "description_path": description_path
        }

    except Exception as e:
        print(f"[ERROR] Download failed: {e}")
        return None
