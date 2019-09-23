import cv2

path = '/home/gabriel-mesquita/Área de Trabalho/speed-detection/speed-detection/resource''/cascades/car.xml'


class FrameController:
    classifier = None

    def __init__(self):
        self.classifier = cv2.CascadeClassifier(path)

    def detect_cars(self, frame_object):
        return self.classifier.detectMultiScale(frame_object.image_processed, 1.1, 13, 18, (24, 24))

