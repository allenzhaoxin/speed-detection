import cv2

from VideoInput import VideoInput

video1 = VideoInput('video_samples/sample_1.mp4')
video2 = VideoInput('video_samples/sample_2.mp4')

# Play video 1

print('Video Sample 1')
print('Width: ', video1.width)
print('Height: ', video1.height)

video1.show_video()

# Play video 1

print('Video Sample 2')
print('Width: ', video2.width)
print('Height: ', video2.height)

video2.show_video()

