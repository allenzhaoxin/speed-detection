import dlib
import cv2

from src.model.Frame import pre_process_frame as pre_process


class TrackController:
    frame_object = None
    cars = None

    carTracker = {}

    last_id = 0

    def remove_tracks(self):
        cars_to_delete = []

        for id in self.carTracker.keys():
            track_quality = self.carTracker[id].update(self.frame_object.image)

            if track_quality < 5:
                cars_to_delete.append(id)

        for id in cars_to_delete:
            print('Removido carro | ID: ' + str(id))
            self.carTracker.pop(id, None)

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

            for carID in self.carTracker.keys():
                tracked_position = self.carTracker[carID].get_position()

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
                    tracked_id = carID

            if tracked_id is None:
                print('Adicionado novo carro | ID: ' + str(self.last_id))

                tracker = dlib.correlation_tracker()

                tracker.start_track(
                    pre_process(frame_object.image),
                    dlib.rectangle(
                        car_start_x,
                        car_start_y,
                        car_start_x + car_end_x,
                        car_start_y + car_end_y
                    )
                )

                self.carTracker[self.last_id] = tracker

                self.last_id = self.last_id + 1

    def print_tracks(self):
        counter = 0
        for id in self.carTracker.keys():
            tracker = self.carTracker[id]
            counter = counter + 1

            tracked_position = tracker.get_position()
            startX = int(tracked_position.left())
            startY = int(tracked_position.top())
            endX = int(tracked_position.right())
            endY = int(tracked_position.bottom())
            cv2.rectangle(self.frame_object.image, (startX, startY), (endX, endY), (0, 0, 255), 2)
            cv2.putText(
                self.frame_object.image,
                'ID: ' + str(id),
                (startX, startY - 15),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.45,
                (0, 250, 0),
                2
            )
