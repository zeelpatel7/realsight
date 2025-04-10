from src.downloader import download_youtube_video

if __name__ == "__main__":
    url = input("Paste a YouTube video URL: ").strip()
    result = download_youtube_video(url)

    if result:
        print("\n[✅ DOWNLOAD COMPLETE]")
        print(f"Video ID: {result['video_id']}")
        print(f"Saved to: {result['video_path']}")
    else:
        print("[❌ SOMETHING WENT WRONG]")




