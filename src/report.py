import os
from datetime import datetime

def generate_report(video_id, title, channel, frame_df, sentiment_result, output_folder="reports"):
    os.makedirs(output_folder, exist_ok=True)
    report_path = os.path.join(output_folder, f"{video_id}_report.md")

    top_frames = frame_df.sort_values(by="suspicion_score", ascending=False).head(5)
    avg_sus = round(frame_df["suspicion_score"].mean(), 4)

    with open(report_path, "w", encoding="utf-8") as f:
        f.write(f"# 🧾 RealSight Forensic Report\n")
        f.write(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        f.write(f"## 🎥 Video Metadata\n")
        f.write(f"- **Video ID:** {video_id}\n")
        f.write(f"- **Title:** {title}\n")
        f.write(f"- **Channel:** {channel}\n\n")
        
        f.write(f"## 🖼️ Frame Analysis\n")
        f.write(f"- **Average Suspicion Score:** {avg_sus}\n")
        f.write(f"- **Top 5 Suspicious Frames:**\n\n")
        f.write(top_frames.to_markdown(index=False))
        f.write("\n\n")

        f.write(f"## 📝 Transcript Sentiment Analysis\n")
        f.write(f"- **Dominant Sentiment:** {sentiment_result['dominant_sentiment']}\n")
        f.write(f"- **Average Score:** {sentiment_result['average_sentiment_score']}\n")
        f.write(f"- **Samples Analyzed:** {sentiment_result['samples_analyzed']}\n\n")
        
        f.write(f"## 🧮 Preliminary Verdict\n")
        f.write(f"This video exhibits a suspicion score of **{avg_sus}**, paired with a primarily **{sentiment_result['dominant_sentiment']}** sentiment profile. Further analysis required to confirm credibility.\n")

    print(f"[✅] Report saved to {report_path}")
