import cv2


class CarsDetection:
    CASCADE_CLASSFIER = None
    cars = []

    def __init__(self):
        self.CASCADE_CLASSFIER = cv2.CascadeClassifier('./../../resource/cascade/car.xml')

    def _pre_process_frame(self, frame):
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        return frame_gray

    def detect(self, frame):
        pre_processed_frame = self._pre_process_frame(frame)
        self.cars = self.CASCADE_CLASSFIER.detectMultiScale(pre_processed_frame, 1.1, 13, 18, (24, 24))
