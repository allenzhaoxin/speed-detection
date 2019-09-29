import cv2


def pre_process_frame(frame):
    return _to_gray(frame)


def _to_gray(frame):
    return cv2.cvtColor(frame.copy(), cv2.COLOR_BGR2GRAY)
