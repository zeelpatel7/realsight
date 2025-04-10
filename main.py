from src.downloader import download_youtube_video
from src.extractor import extract_frames, extract_audio
from src.analyzer import analyze_frames, analyze_transcript
from src.report import generate_report
import os

if __name__ == "__main__":
    url = input("Paste a YouTube video URL: ").strip()
    result = download_youtube_video(url)

    if result:
        video_id = result['video_id']
        title = result['title']
        channel = result['channel']
        base_path = os.path.join("data", video_id)

        print("\n[✅ DOWNLOAD COMPLETE]")
        print(f"Video ID: {video_id}")
        print(f"Saved to: {base_path}")

        # Extract frames and audio
        frames_path = os.path.join(base_path, "frames")
        extract_frames(result["video_path"], frames_path)

        audio_path = os.path.join(base_path, "audio.wav")
        extract_audio(result["video_path"], audio_path)

        # Analyze frames and transcript
        print("\n[🔎 ANALYZING FRAMES...]")
        frame_df = analyze_frames(frames_path)

        print("\n[📝 ANALYZING TRANSCRIPT...]")
        sentiment_result = analyze_transcript(result["transcript_path"])

        # Generate final report
        generate_report(video_id, title, channel, frame_df, sentiment_result)

    else:
        print("[❌ SOMETHING WENT WRONG]")
