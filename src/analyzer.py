import os
import torch
import torchvision.transforms as transforms
from PIL import Image
from transformers import pipeline
import pandas as pd

# === MODEL: Placeholder GAN Artifact Classifier (ResNet Pretrained ===
# Note: Replace this with an actual deepfake classifier later
def load_frame_model():
    model = torch.hub.load('pytorch/vision:v0.10.0', 'resnet18', pretrained=True)
    model.eval()
    return model

def analyze_frames(folder_path="data/frames"):
    model = load_frame_model()

    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor()
    ])

    results = []

    for file in os.listdir(folder_path):
        if file.endswith(".jpg"):
            path = os.path.join(folder_path, file)
            image = Image.open(path).convert("RGB")
            tensor = transform(image).unsqueeze(0)

            with torch.no_grad():
                output = model(tensor)
                confidence = torch.nn.functional.softmax(output[0], dim=0).max().item()

            results.append({
                "frame": file,
                "suspicion_score": round(1 - confidence, 4)  # Invert as a fake-likelihood proxy
            })

    return pd.DataFrame(results)


# === TRANSCRIPT SENTIMENT ANALYSIS ===

def analyze_transcript(transcript_path):
    classifier = pipeline("sentiment-analysis")

    with open(transcript_path, "r", encoding="utf-8") as f:
        text = f.read()

    chunks = [text[i:i+512] for i in range(0, len(text), 512)]
    sentiments = classifier(chunks)

    df = pd.DataFrame(sentiments)
    avg_score = df["score"].mean()
    dominant = df["label"].mode()[0]

    return {
        "average_sentiment_score": round(avg_score, 3),
        "dominant_sentiment": dominant,
        "samples_analyzed": len(df)
    }
