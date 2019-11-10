import cv2
import os

from src.controller.VideoController import VideoController


class VideoViewer:
    MODE_RUN_AND_PLAY = 1
    MODE_PRE_COMPILE = 2
    MODE_OUTPUT = 3

    video_controller = None
    path = None

    def __init__(self, path, pixels_per_meters):
        self.path = path
        self.video_controller = VideoController(self.path, pixels_per_meters)

    def run(self, mode=1):
        if mode == self.MODE_RUN_AND_PLAY:
            self.video_controller.is_to_print_pre_process_progress = False
            self._run_and_play()
        elif mode == self.MODE_PRE_COMPILE:
            self.video_controller.is_to_print_pre_process_progress = True
            self._pre_compile()
        elif mode == self.MODE_OUTPUT:
            self.video_controller.is_to_print_pre_process_progress = True
            self._output()
        else:
            print('[ERROR] Param \'mode\' invalid!')

        cv2.destroyAllWindows()

    def _run_and_play(self):
        while len(self.video_controller.frames) != self.video_controller.total_frames:
            frame_object = self.video_controller.pre_process()

            cv2.imshow('RUN_AND_PLAY_MODE ', frame_object.image)
            key = cv2.waitKey(20) & 0xFF

    def _pre_compile(self):
        while len(self.video_controller.frames) != self.video_controller.total_frames:
            self.video_controller.pre_process()

        for frame_object in self.video_controller.frames:
            cv2.imshow('PRE_COMPILE_MODE ', frame_object.image)
            key = cv2.waitKey(20) & 0xFF

    def _output(self):
        filename = os.path.splitext(os.path.basename(self.path))[0]
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'resource', 'video_samples',
                            'output', str(filename + '.mp4'))

        out = cv2.VideoWriter(path, 0x7634706d,
                              self.video_controller.video_input.get_fps(),
                              (int(self.video_controller.video_input.width),
                               int(self.video_controller.video_input.height)))

        while len(self.video_controller.frames) != self.video_controller.total_frames:
            frame_object = self.video_controller.pre_process()
            out.write(frame_object.image)

        out.release()
