import cv2

from src.controller.CarsDetection import CarsDetection
from src.view.VideoInput import VideoInput


class VideoController:
    videoInput = None
    frames = []

    def __init__(self, path):
        self.videoInput = VideoInput(path)

        if self.videoInput.is_restarted_video():
            count = 0
            there_are_more_frames = True
            while there_are_more_frames:
                there_are_more_frames, image = self.videoInput.video.read()

                # Saves the frames with frame-count
                self.frames.append(image)

                count += 1
            print(len(self.frames))
