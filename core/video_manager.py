"""
============================================================
AI Surveillance System
Video Manager
============================================================
Author : Dheeraj
============================================================
"""

import cv2

import config
from core.logger import Logger


class VideoManager:

    def __init__(self):

        self.logger = Logger()

        self.capture = None

        self.writer = None

    # -----------------------------------------------------

    def open_video(self, source=None):

        if source is None:

            source = str(config.VIDEO_SOURCE)

        self.capture = cv2.VideoCapture(source)

        if not self.capture.isOpened():

            self.logger.error(
                "Unable to Open Video."
            )

            return False

        self.logger.info(
            f"Video Opened : {source}"
        )

        return True

    # -----------------------------------------------------

    def read(self):

        if self.capture is None:

            return False, None

        return self.capture.read()

    # -----------------------------------------------------

    def create_output(self, width, height, fps=30):

        output_path = str(

            config.OUTPUT_VIDEO_DIR /
            "output.mp4"

        )

        fourcc = cv2.VideoWriter_fourcc(*"mp4v")

        self.writer = cv2.VideoWriter(

            output_path,

            fourcc,

            fps,

            (width, height)

        )

        self.logger.info(

            f"Output Video : {output_path}"

        )

    # -----------------------------------------------------

    def write(self, frame):

        if self.writer is not None:

            self.writer.write(frame)

    # -----------------------------------------------------

    def release(self):

        if self.capture is not None:

            self.capture.release()

        if self.writer is not None:

            self.writer.release()

        cv2.destroyAllWindows()

        self.logger.info("Video Closed")

    # -----------------------------------------------------

    def get_width(self):

        return int(

            self.capture.get(

                cv2.CAP_PROP_FRAME_WIDTH

            )

        )

    # -----------------------------------------------------

    def get_height(self):

        return int(

            self.capture.get(

                cv2.CAP_PROP_FRAME_HEIGHT

            )

        )

    # -----------------------------------------------------

    def get_fps(self):

        return int(

            self.capture.get(

                cv2.CAP_PROP_FPS

            )

        )

    # -----------------------------------------------------

    def get_frame_count(self):

        return int(

            self.capture.get(

                cv2.CAP_PROP_FRAME_COUNT

            )

        )
