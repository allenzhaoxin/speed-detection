import cv2

from src.controller.VideoController import VideoController


class VideoViewer:
    MODE_RUN_AND_PLAY = 1
    MODE_PRE_COMPILE = 2

    video_controller = None

    def __init__(self, path, pixels_per_meters):
        self.video_controller = VideoController(path, pixels_per_meters)

    def run(self, mode=1):
        if mode == self.MODE_RUN_AND_PLAY:
            self.video_controller.is_to_print_pre_process_progress = False
            self._run_and_play()
        elif mode == self.MODE_PRE_COMPILE:
            self.video_controller.is_to_print_pre_process_progress = True
            self._pre_compile()
        else:
            print('[ERROR] Param \'mode\' invalid!')

    def _run_and_play(self):
        while len(self.video_controller.frames) != self.video_controller.total_frames:

            frame_object = self.video_controller.pre_process()

            cv2.imshow('RUN_AND_PLAY_MODE ', frame_object.image)
            key = cv2.waitKey(20) & 0xFF

    def _pre_compile(self):
        while len(self.video_controller.frames) != self.video_controller.total_frames:

            self.video_controller.pre_process()

        for frame in self.video_controller.frames:
            cv2.imshow('PRE_COMPILE_MODE ', frame.image)
            key = cv2.waitKey(20) & 0xFF
