import os
import torch
import torchvision.transforms as transforms
from PIL import Image
from transformers import pipeline
import pandas as pd
from torchvision.models import resnet18, ResNet18_Weights

# === MODEL: Placeholder GAN Artifact Classifier (ResNet Pretrained ===
# Note: Replace this with an actual deepfake classifier later
def load_frame_model():
    model = resnet18(weights=ResNet18_Weights.IMAGENET1K_V1)
    model.eval()
    return model

def analyze_frames(folder_path="data/frames"):
    model = load_frame_model()
    
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = model.to(device)

    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor()
    ])

    results = []

    for file in os.listdir(folder_path):
        if file.endswith(".jpg"):
            path = os.path.join(folder_path, file)
            with Image.open(path).convert("RGB") as image:
                tensor = transform(image).unsqueeze(0).to(device)

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
    classifier = pipeline(
    "sentiment-analysis", 
    model="distilbert-base-uncased-finetuned-sst-2-english", 
    framework="pt"  # Force PyTorch backend
)

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
