from src.view.VideoInput import VideoInput

video1 = VideoInput('resource/video_samples/sample_1.mp4')
video2 = VideoInput('resource/video_samples/sample_2.mp4')
video3 = VideoInput('resource/video_samples/sample_3.mp4')
video4 = VideoInput('resource/video_samples/sample_4.mp4')

# Play video 1

print('Video Sample 1')
print('Width: ', video1.width)
print('Height: ', video1.height)

video1.show_video()

# Play video 2

print('Video Sample 2')
print('Width: ', video2.width)
print('Height: ', video2.height)

video2.show_video()

# Play video 3

print('Video Sample 3')
print('Width: ', video3.width)
print('Height: ', video3.height)

video3.show_video()

# Play video 4

print('Video Sample 4')
print('Width: ', video4.width)
print('Height: ', video4.height)

video4.show_video()
