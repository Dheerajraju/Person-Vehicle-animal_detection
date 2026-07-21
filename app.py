"""
============================================================
AI Surveillance System
Stage 2
Real-Time Object Detection
============================================================
Author : Dheeraj
============================================================
"""

import cv2
import time

import config

from core.logger import Logger
from core.video_manager import VideoManager
from core.detector import Detector


class AISurveillanceSystem:

    def __init__(self):

        self.logger = Logger()

        self.video = VideoManager()

        self.detector = Detector()

    # ---------------------------------------------------------

    def banner(self):

        print()

        print("=" * 60)
        print(config.PROJECT_NAME)
        print("Stage 2 : Real-Time Object Detection")
        print("=" * 60)
        print()

    # ---------------------------------------------------------

    def start(self):

        self.banner()

        self.logger.info("Application Started")

        if not self.video.open_video():

            self.logger.error("Cannot Open Video")

            return

        width = self.video.get_width()

        height = self.video.get_height()

        fps = self.video.get_fps()

        self.video.create_output(

            width,

            height,

            fps

        )

        previous_time = time.time()

        while True:

            ret, frame = self.video.read()

            if not ret:

                self.logger.info("Video Finished")

                break

            # ----------------------------------------
            # Detection
            # ----------------------------------------

            detections = self.detector.detect(frame)

            frame = self.detector.draw(

                frame,

                detections

            )

            # ----------------------------------------
            # Statistics
            # ----------------------------------------

            counts = self.detector.count_objects(

                detections

            )

            # ----------------------------------------
            # FPS
            # ----------------------------------------

            current_time = time.time()

            fps = 1 / (current_time - previous_time)

            previous_time = current_time

            # ----------------------------------------
            # Draw FPS
            # ----------------------------------------

            cv2.putText(

                frame,

                f"FPS : {fps:.2f}",

                (20, 35),

                cv2.FONT_HERSHEY_SIMPLEX,

                0.8,

                (0, 255, 0),

                2

            )

            # ----------------------------------------
            # Draw Object Counts
            # ----------------------------------------

            y = 70

            for cls, total in counts.items():

                cv2.putText(

                    frame,

                    f"{cls} : {total}",

                    (20, y),

                    cv2.FONT_HERSHEY_SIMPLEX,

                    0.7,

                    (255, 255, 255),

                    2

                )

                y += 30

            # ----------------------------------------
            # Save Output
            # ----------------------------------------

            self.video.write(frame)

            # ----------------------------------------
            # Display
            # ----------------------------------------

            cv2.imshow(

                config.PROJECT_NAME,

                frame

            )

            key = cv2.waitKey(1)

            if key & 0xFF == ord("q"):

                self.logger.info("Exit Requested")

                break

        self.video.release()

        self.logger.info("Application Closed")


def main():

    app = AISurveillanceSystem()

    app.start()


if __name__ == "__main__":

    main()
