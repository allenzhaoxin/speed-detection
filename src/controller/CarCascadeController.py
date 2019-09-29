import cv2

from src.controller.PreProcessController import pre_process_frame

path = '/home/gabriel-mesquita/Área de Trabalho/speed-detection/speed-detection/resource''/cascades/car.xml'


class CarCascadeController:

    classifier = None

    def __init__(self):
        self.classifier = cv2.CascadeClassifier(path)

    def detect_cars(self, frame_object):
        return self.classifier.detectMultiScale(pre_process_frame(frame_object.image), 1.1, 13, 18, (24, 24))

