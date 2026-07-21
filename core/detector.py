"""
============================================================
AI Surveillance System
Detection Engine
============================================================
"""

import cv2

import config

from core.logger import Logger

from core.model_loader import ModelLoader


class Detector:

    def __init__(self):

        self.logger = Logger()

        self.model_loader = ModelLoader()

        self.model = self.model_loader.load()

        self.names = self.model.names

        self.logger.info("Detector Initialized")

    # -----------------------------------------------------

    def detect(self, frame):

        detections = []

        results = self.model.predict(

            source=frame,

            conf=config.CONFIDENCE_THRESHOLD,

            iou=config.IOU_THRESHOLD,

            imgsz=config.IMAGE_SIZE,

            device=config.DEVICE,

            verbose=False

        )

        for result in results:

            boxes = result.boxes

            for box in boxes:

                cls = int(box.cls[0])

                name = self.names[cls]

                if name not in config.TARGET_CLASSES:

                    continue

                conf = float(box.conf[0])

                x1, y1, x2, y2 = map(

                    int,

                    box.xyxy[0]

                )

                detections.append(

                    {

                        "class": name,

                        "confidence": conf,

                        "box": (

                            x1,

                            y1,

                            x2,

                            y2

                        )

                    }

                )

        return detections

    # -----------------------------------------------------

    def draw(self, frame, detections):

        for obj in detections:

            x1, y1, x2, y2 = obj["box"]

            cls = obj["class"]

            conf = obj["confidence"]

            color = config.CLASS_COLORS.get(

                cls,

                (255, 255, 255)

            )

            cv2.rectangle(

                frame,

                (x1, y1),

                (x2, y2),

                color,

                2

            )

            label = f"{cls} {conf:.2f}"

            cv2.putText(

                frame,

                label,

                (x1, y1 - 8),

                cv2.FONT_HERSHEY_SIMPLEX,

                0.6,

                color,

                2

            )

        return frame

    # -----------------------------------------------------

    def count_objects(

        self,

        detections

    ):

        counts = {}

        for obj in detections:

            cls = obj["class"]

            if cls not in counts:

                counts[cls] = 0

            counts[cls] += 1

        return counts

    # -----------------------------------------------------

    def print_statistics(

        self,

        counts

    ):

        print()

        print("=" * 40)

        print("Detected Objects")

        print("=" * 40)

        for key, value in counts.items():

            print(f"{key:15} : {value}")

        print("=" * 40)
