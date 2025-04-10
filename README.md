# RealSight 🎥🕵️‍♀️
**AI-powered forensic analysis of online video content**

RealSight is a machine learning pipeline designed to detect manipulated, AI-generated, or misleading videos posted online. Unlike simple deepfake detectors, RealSight combines evidence across multiple modalities — visual, audio, textual, and contextual — and outputs a structured, explainable forensic report.

This isn't just a "true or false" detector. This is an AI content prosecutor with receipts.

---

## 🔍 What It Does

- 🎞️ **Video Frame Analysis:** Detects visual anomalies, GAN-generated features, reused footage
- 🔊 **Audio Extraction:** Analyzes speech patterns and checks for voice synthesis
- 📝 **Caption & Transcript Review:** Extracts claims, checks emotional language, verifies consistency
- 🌐 **Context Verification:** Reverse image search and metadata inspection to flag content repurposing
- 🧮 **Bayesian Credibility Modeling:** Integrates all evidence to compute a final credibility score
- 🧾 **Structured Forensic Report:** Outputs explainable results for transparency and trust

---

## ✅ Current Progress

- [x] ✅ YouTube video downloader via `yt-dlp`
- [x] ✅ Captions + metadata extraction
- [x] ✅ FFmpeg integration for video/audio merging
- [ ] ⬜ Frame and audio analysis (coming next)
- [ ] ⬜ NLP + claim extraction + verification
- [ ] ⬜ Bayesian model scoring
- [ ] ⬜ PDF/Markdown report generation

---

## 🧠 Why This Matters

Disinformation is spreading faster than ever. Deepfakes, fake war footage, and AI-generated propaganda are being shared without context — often with malicious intent. RealSight helps fight back by providing:

> 🔦 **Transparent, explainable, and evidence-based media verification.**

Built for researchers, educators, journalists, and anyone who doesn’t want to be manipulated by a high-res lie.

---

## 🚀 How to Use

1. Clone the repo
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
