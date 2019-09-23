import cv2

path = '/home/gabriel-mesquita/Área de Trabalho/speed-detection/speed-detection/resource''/cascades/car.xml'


def _pre_process_frame(frame):
    return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


class FrameController:
    classifier = None

    def __init__(self):
        self.classifier = cv2.CascadeClassifier(path)

    def detect_cars(self, frame):
        processed_frame = _pre_process_frame(frame)
        return self.classifier.detectMultiScale(processed_frame, 1.1, 4)
