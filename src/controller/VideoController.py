from src.view.VideoInput import VideoInput
from src.controller.TrackController import track_cars
from src.controller.FrameController import FrameController
from src.model.Frame import Frame

import cv2


class VideoController:
    video_input = None

    frames = []

    def __init__(self, path):
        self.video_input = VideoInput(path)
        self.discover_video_frames()

        for frame in self.frames:
            print(frame.cars)

    def discover_video_frames(self):
        if self.video_input.is_restarted_video():

            there_are_more_frames = True
            frame_controller = FrameController()

            while there_are_more_frames:
                there_are_more_frames, frame = self.video_input.video.read()

                if not there_are_more_frames:
                    break

                frame_object = Frame(frame)

                frame_object.cars = frame_controller.detect_cars(frame_object)

                track_cars(frame_object)

                self.frames.append(frame_object)

                cv2.imshow('a', frame_object.image)
                key = cv2.waitKey(1) & 0xFF
