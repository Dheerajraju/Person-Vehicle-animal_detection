"""
============================================================
AI Surveillance System
Model Loader Engine
============================================================
"""
from pathlib import Path
from ultralytics import YOLO, RTDETR
import config
from core.logger import Logger


class ModelLoader:
    def __init__(self):
        self.logger = Logger()
        self.model_path = config.MODEL_PATH

    def load(self):
        self.logger.info(f"Loading Model: {self.model_path.name}")
        
        # Check if the requested model is a Vision Transformer (RT-DETR)
        if "rtdetr" in self.model_path.name.lower():
            self.logger.info("Using RT-DETR Vision Transformer Engine...")
            return RTDETR(self.model_path)
        
        # Default to standard YOLO engine (YOLOv8, v10, 11, 12 etc.)
        return YOLO(self.model_path)
