import cv2


class VideoInput:
    _path = None
    width = None
    height = None
    video = None

    def __init__(self, path):
        self._path = path
        self.load_video()

    def load_video(self):
        self.video = cv2.VideoCapture(self._path)
        self.capture_dimension()

    def capture_dimension(self):
        if self.video.isOpened():
            self.width = self.video.get(3)
            self.height = self.video.get(4)
        else:
            print("Error opening video stream or file")

    def is_restarted_video(self):
        return self.video.set(cv2.CAP_PROP_POS_AVI_RATIO, 0)

    def show_fps(self):
        return self.video.get(cv2.CAP_PROP_FPS)

    def show_frames_count(self):
        return self.video.get(cv2.CAP_PROP_POS_FRAMES)

    def show_video(self):
        if self.video.isOpened():
            while self.video.isOpened():
                # Capture frame-by-frame
                ret, frame = self.video.read()
                if ret == True:

                    # Display the resulting frame
                    cv2.imshow('Video: ' + str(self._path) + ' (press Q to EXIT)', frame)

                    # Press Q on keyboard to  exit
                    if cv2.waitKey(25) & 0xFF == ord('q'):
                        break

                # Break the loop
                else:
                    break
        else:
            print("Error opening video stream or file")

        # When everything done, release the video capture object
        self.video.release()

        # Closes all the frames
        cv2.destroyAllWindows()
