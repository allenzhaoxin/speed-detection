import dlib
import cv2

trackers = []


def track_cars(frame_object):
    for (_x, _y, _w, _h) in frame_object.cars:
        x = int(_x)
        y = int(_y)
        w = int(_w)
        h = int(_h)

        tracker = dlib.correlation_tracker()

        rect = dlib.rectangle(x, y, x + w, y + h)
        tracker.start_track(frame_object.image_processed, rect)

        trackers.append(tracker)

        print("New tracked car")

    for t in trackers:
        t.update(frame_object.image)
        pos = t.get_position()
        startX = int(pos.left())
        startY = int(pos.top())
        endX = int(pos.right())
        endY = int(pos.bottom())
        cv2.rectangle(frame_object.image, (startX, startY), (endX, endY), (0, 255, 0), 2)

    return trackers
