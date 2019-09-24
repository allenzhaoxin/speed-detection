from src.view.VideoInput import VideoInput

from src.controller.TrackController import track_cars, print_tracks
from src.controller.FrameController import FrameController

from src.model.Frame import Frame


class VideoController:
    video_input = None

    frames = []
    total_frames = 1

    def __init__(self, path):
        self.video_input = VideoInput(path)
        self.total_frames = self.video_input.get_frames_count()
        self.process()

    def is_process_ready(self):
        current_frames = len(self.frames)

        is_ready = False

        if current_frames >= self.total_frames:
            is_ready = True

        process_percentage = ((current_frames / self.total_frames) * 100)

        return is_ready, process_percentage

    def process(self):
        if self.video_input.is_restarted_video():

            there_are_more_frames = True
            frame_controller = FrameController()

            while there_are_more_frames:
                there_are_more_frames, frame = self.video_input.video.read()

                if not there_are_more_frames:
                    break

                frame_object = Frame(frame)

                cars = frame_controller.detect_cars(frame_object)

                trackers, labels = track_cars(frame_object, cars)

                print_tracks(frame_object, trackers, labels)

                self.frames.append(frame_object)

                self.is_process_ready()

                is_process_ready, process_percentage = self.is_process_ready()
                print('Processing [' + str(int(process_percentage)) + '%] | Finished: ' + str(is_process_ready))
