import dlib
import cv2

from src.controller.PreProcessController import pre_process_frame


class TrackController:
    speed_controller = None

    frame_object = None
    cars = None

    carTracker = {}
    carSpeed = {}

    last_id = 0

    def __init__(self, speed_controller):
        self.speed_controller = speed_controller

    def remove_tracks(self):
        cars_to_delete = []

        for id in self.carTracker.keys():
            track_quality = self.carTracker[id].update(self.frame_object.image)

            if track_quality < 5:
                cars_to_delete.append(id)

        for id in cars_to_delete:
            self.carTracker.pop(id, None)

    def add_new_track(self, car_start_x, car_start_y, car_end_x, car_end_y):

        tracker = dlib.correlation_tracker()

        tracker.start_track(
            pre_process_frame(self.frame_object.image),
            dlib.rectangle(
                car_start_x,
                car_start_y,
                car_start_x + car_end_x,
                car_start_y + car_end_y
            )
        )

        self.carTracker[self.last_id] = tracker
        self.carSpeed[self.last_id] = 0
        self.last_id = self.last_id + 1

    def track_cars(self, frame_object, cars):

        self.remove_tracks()

        self.frame_object = frame_object

        for (car_sx, car_sy, car_ex, car_ey) in cars:
            car_start_x = int(car_sx)
            car_start_y = int(car_sy)
            car_end_x = int(car_ex)
            car_end_y = int(car_ey)

            max_x = car_start_x + 0.5 * car_end_x
            max_y = car_start_y + 0.5 * car_end_y

            tracked_id = None

            for car_id in self.carTracker.keys():
                tracked_position = self.carTracker[car_id].get_position()

                tracked_start_x = int(tracked_position.left())
                tracked_start_y = int(tracked_position.top())
                tracked_end_x = int(tracked_position.width())
                tracked_end_y = int(tracked_position.height())

                max_tracked_x = tracked_start_x + 0.5 * tracked_end_x
                max_tracked_y = tracked_start_y + 0.5 * tracked_end_y

                if (tracked_start_x <= max_x <= (tracked_start_x + tracked_end_x)) and (
                        not tracked_start_y <= max_y > (tracked_start_y + tracked_end_y)) and (
                        not car_start_x <= max_tracked_x > (car_start_x + car_end_x)) and (
                        not car_start_y <= max_tracked_y > (car_start_y + car_end_y)):
                    tracked_id = car_id

                if self.carSpeed[car_id] == 0:
                    self.carSpeed[car_id] = self.speed_controller.speed_calculation([car_start_x, car_start_y, car_end_x, car_end_y], [tracked_start_x, tracked_start_y, tracked_end_x,tracked_end_y])

                    if self.carSpeed[car_id] > 150:
                        self.carSpeed[car_id] = 0

            if tracked_id is None:
                self.add_new_track(car_start_x, car_start_y, car_end_x, car_end_y)

    def print_tracks(self):
        counter = 0
        for id in self.carTracker.keys():
            tracker = self.carTracker[id]
            counter = counter + 1

            tracked_position = tracker.get_position()
            start_x = int(tracked_position.left())
            start_y = int(tracked_position.top())
            end_x = int(tracked_position.right())
            end_y = int(tracked_position.bottom())
            cv2.rectangle(self.frame_object.image, (start_x, start_y), (end_x, end_y), (0, 0, 255), 2)
            cv2.putText(
                self.frame_object.image,
                'ID: ' + str(id),
                (start_x, start_y - 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.45,
                (0, 250, 0),
                2
            )
            cv2.putText(
                self.frame_object.image,
                'VEL.: ' + str(int(self.carSpeed[id])) + ' KM/H',
                (start_x, start_y - 15),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.45,
                (200, 250, 250),
                2
            )
