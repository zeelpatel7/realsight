import yt_dlp
import os

def download_youtube_video(url, save_path="data"):
    try:
        print(f"[INFO] Starting download for {url}")

        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': f'{save_path}/%(id)s.%(ext)s',
            'writeinfojson': True,
            'writedescription': True,
            'writeautomaticsub': True,
            'writesubtitles': True,
            'subtitleslangs': ['en'],
            'quiet': False,
            'ffmpeg_location': 'C:\\Program Files\\ffmpeg\\ffmpeg-7.1.1-essentials_build\\bin',
            'http_headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
                'Accept-Language': 'en-US,en;q=0.9',
            }
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)

        video_id = info_dict.get("id")
        title = info_dict.get("title")
        description = info_dict.get("description")
        channel = info_dict.get("uploader")

        print(f"[INFO] Download complete for video: {title}")

        return {
            "video_id": video_id,
            "title": title,
            "description": description,
            "channel": channel,
            "video_path": os.path.join(save_path, f"{video_id}.mp4")
        }

    except Exception as e:
        print(f"[ERROR] Download failed: {e}")
        return None
