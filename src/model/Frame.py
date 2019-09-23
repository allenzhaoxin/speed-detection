import cv2


def _pre_process_frame(frame):
    return cv2.cvtColor(frame.copy(), cv2.COLOR_BGR2GRAY)


class Frame:
    image = None
    image_processed = None

    cars = []

    def __init__(self, image):
        self.image = image
        self.image_processed = _pre_process_frame(self.image)
