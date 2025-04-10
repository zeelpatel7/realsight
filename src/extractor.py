import os
import subprocess
import cv2

def extract_frames(video_path, output_folder, frame_rate=1):
    os.makedirs(output_folder, exist_ok=True)

    vidcap = cv2.VideoCapture(video_path)
    fps = vidcap.get(cv2.CAP_PROP_FPS)
    interval = int(fps * frame_rate)

    count = 0
    frame_id = 0

    print(f"[INFO] Extracting frames from {video_path}")

    while True:
        success, frame = vidcap.read()
        if not success:
            break
        if count % interval == 0:
            frame_path = os.path.join(output_folder, f"frame_{frame_id:04d}.jpg")
            cv2.imwrite(frame_path, frame)
            frame_id += 1
        count += 1

    vidcap.release()
    print(f"[INFO] Extracted {frame_id} frames to {output_folder}")

def extract_audio(video_path, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    print(f"[INFO] Extracting audio from {video_path}")
    cmd = [
        "ffmpeg",
        "-i", video_path,
        "-vn",
        "-acodec", "pcm_s16le",
        "-ar", "44100",
        "-ac", "2",
        output_path
    ]

    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"[INFO] Audio saved to {output_path}")
