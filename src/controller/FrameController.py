import cv2

from src.model.Frame import pre_process_frame as pre_process

path = '/home/gabriel-mesquita/Área de Trabalho/speed-detection/speed-detection/resource''/cascades/car.xml'


class FrameController:
    classifier = None

    def __init__(self):
        self.classifier = cv2.CascadeClassifier(path)

    def detect_cars(self, frame_object):
        return self.classifier.detectMultiScale(pre_process(frame_object.image), 1.1, 13, 18, (24, 24))

