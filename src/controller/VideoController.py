from src.controller.VideoInput import VideoInput
from src.controller.TrackController import TrackController
from src.controller.CarCascadeController import CarCascadeController
from src.controller.SpeedController import SpeedController

from src.model.Frame import Frame


class VideoController:
    video_input = None

    car_cascade_controller = None
    track_controller = None
    speed_controller = None

    frames = []
    total_frames = 1

    is_to_print_pre_process_progress = True

    def __init__(self, path, pixels_per_meters):
        self.car_cascade_controller = CarCascadeController()
        self.video_input = VideoInput(path)
        self.speed_controller = SpeedController(pixels_per_meters)
        self.track_controller = TrackController(self.speed_controller)
        self.video_input.restart_video()
        self.total_frames = self.video_input.get_frames_count()

    def _process_frame(self, frame):

        frame_object = Frame(frame)

        cars = self.car_cascade_controller.detect_cars(frame_object)

        self.track_controller.track_cars(frame_object, cars)
        self.track_controller.print_tracks()

        self.start_progression_counter()

        self.speed_controller.frames_per_second = self.video_input.get_fps()

        return frame_object

    def _next_frame(self):
        there_are_more_frames = True

        while there_are_more_frames:
            there_are_more_frames, frame = self.video_input.video.read()

            return there_are_more_frames, frame

    def pre_process(self):
        there_are_more_frames, frame = self._next_frame()

        if there_are_more_frames:
            frame_object = self._process_frame(frame)
            self.frames.append(frame_object)

            return frame_object

    def start_progression_counter(self):
        current_frames = len(self.frames)

        process_percentage = ((current_frames / self.total_frames) * 100)

        if self.is_to_print_pre_process_progress:
            print('Processing [' + str(int(process_percentage)) + '%]')

        return process_percentage
