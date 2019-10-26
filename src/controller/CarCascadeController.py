import os.path
import cv2

from src.controller.PreProcessController import pre_process_frame


class CarCascadeController:

    classifier = None

    def __init__(self):
        ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
        CASCADE_PATH = os.path.join(ROOT_DIR, '..', '..', 'resource', 'cascades', 'car.xml')

        self.classifier = cv2.CascadeClassifier(CASCADE_PATH)

    def detect_cars(self, frame_object):
        return self.classifier.detectMultiScale(pre_process_frame(frame_object.image), 1.1, 13, 18, (24, 24))

