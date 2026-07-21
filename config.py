"""
============================================================
AI Surveillance System
Configuration File
============================================================
"""

from pathlib import Path

# ============================================================
# Project Information
# ============================================================

PROJECT_NAME = "AI Surveillance System"
VERSION = "1.0.0"

# ============================================================
# Base Directory
# ============================================================

BASE_DIR = Path(__file__).resolve().parent

MODELS_DIR = BASE_DIR / "models"

VIDEOS_DIR = BASE_DIR / "videos"

INPUT_VIDEO_DIR = VIDEOS_DIR / "input"

OUTPUT_VIDEO_DIR = VIDEOS_DIR / "output"

OUTPUT_DIR = BASE_DIR / "output"

REPORT_DIR = BASE_DIR / "reports"

LOG_DIR = BASE_DIR / "logs"

# ============================================================
# Model
# ============================================================

DEFAULT_MODEL = "yolo11s.pt"

MODEL_PATH = MODELS_DIR / DEFAULT_MODEL

# ============================================================
# Video
# ============================================================

VIDEO_SOURCE = INPUT_VIDEO_DIR / "Camera_D3.mp4"

# ============================================================
# Detection
# ============================================================

CONFIDENCE_THRESHOLD = 0.40

IOU_THRESHOLD = 0.45

IMAGE_SIZE = 640

DEVICE = "cpu"

# ============================================================
# COCO Classes
# ============================================================

TARGET_CLASSES = [

    "person",

    "bicycle",

    "car",

    "motorcycle",

    "bus",

    "truck",

    "dog",

    "cat",

    "bird"

]

# ============================================================
# Colors (BGR)
# ============================================================

CLASS_COLORS = {

    "person": (0, 255, 0),

    "car": (255, 0, 0),

    "bus": (0, 255, 255),

    "truck": (0, 0, 255),

    "motorcycle": (255, 255, 0),

    "bicycle": (255, 0, 255),

    "dog": (0, 128, 255),

    "cat": (255, 128, 0),

    "bird": (128, 255, 0)

}

# ============================================================
# Logging
# ============================================================

LOG_FILE = LOG_DIR / "system.log"

# ============================================================
# Create folders automatically
# ============================================================

for folder in [

    MODELS_DIR,

    INPUT_VIDEO_DIR,

    OUTPUT_VIDEO_DIR,

    OUTPUT_DIR,

    REPORT_DIR,

    LOG_DIR

]:

    folder.mkdir(parents=True, exist_ok=True)
