import cv2

cascade = cv2.CascadeClassifier('/home/gabriel-mesquita/Área de Trabalho/speed-detection/speed-detection/resource'
                                '/cascades/car.xml')


class FrameController:
    frame = None

    cars = None

    def __init__(self, frame):
        self.frame = frame.copy()
        self.detect_cars()

    def _pre_process_frame(self):
        frame_gray = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)

        return frame_gray

    def detect_cars(self):
        processed_frame = self._pre_process_frame()
        self.cars = cascade.detectMultiScale(processed_frame, 1.1, 4)
