import cv2

from VideoInput import VideoInput

video = VideoInput('example1.mp4')

print('Width: ', video.width)
print('Height: ', video.height)

video.show_video()
