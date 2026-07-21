"""
============================================================
AI Surveillance System
Model Pre-downloader
============================================================
"""
from pathlib import Path
from ultralytics import YOLO

# Define the models directory
BASE_DIR = Path(__file__).resolve().parent
MODELS_DIR = BASE_DIR / "models"
MODELS_DIR.mkdir(parents=True, exist_ok=True)

# List of models you might want to switch between
MODELS_TO_DOWNLOAD = [
    "yolov8n.pt",
    "yolov8s.pt",
    "yolo11n.pt",
    "yolo11s.pt",
]

print("=" * 60)
print("Downloading requested YOLO models into /models directory...")
print("=" * 60)

for model_name in MODELS_TO_DOWNLOAD:
    target_path = MODELS_DIR / model_name
    print(f"\n[INFO] Processing: {model_name}")
    
    if target_path.exists():
        print(f"[✔] already exists locally at: {target_path}")
    else:
        print(f"[↓] Downloading {model_name} from Ultralytics...")
        # This downloads it to the root first, then we safely move it to /models
        model = YOLO(model_name)
        temp_path = Path(model_name)
        if temp_path.exists():
            temp_path.rename(target_path)
            print(f"[✔] Successfully saved to: {target_path}")

print("\n" + "=" * 60)
print("All downloads finished! You can delete this script or keep it.")
print("=" * 60)
