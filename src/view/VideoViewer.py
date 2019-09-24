import cv2

from src.controller.VideoController import VideoController


class VideoViewer:
    video_controller = None

    def __init__(self, path):
        self.video_controller = VideoController(path)

        for frame in self.video_controller.frames:
            cv2.imshow('Path: ' + path, frame.image)
            key = cv2.waitKey(10) & 0xFF
