from src.view.VideoViewer import VideoViewer

# ---------------------------------------------------------- #
#                     SPEED DETECTION                        #
#             Author: Gabriel Teixeira Mesquita              #
# ---------------------------------------------------------- #
#                     VIDEO VIEWER MODES:                    #
#                                                            #
#  1 - MODE_RUN_AND_PLAY -> SHOW THE VIDEO WITCH EACH FRAME  #
#  2 - MODE_PRE_COMPILE  -> PROCESS ALL FRAME AFTER SHOW     #
#  3 - MODE_OUTPUT       -> GENERATES A OUTPUT VIDEO FILE    #
# ---------------------------------------------------------- #
# ---------------------------------------------------------- #


# VIDEO SAMPLES - DAY 1

video = VideoViewer('resource/video_samples/input/teste_controlado_60_day1.mp4', 19)
video.run(VideoViewer.MODE_RUN_AND_PLAY)

# video = VideoViewer('resource/video_samples/input/teste_controlado_80_day1.mp4', 19)
# video.run(VideoViewer.MODE_OUTPUT)

# video = VideoViewer('resource/video_samples/input/teste_controlado_100_day1.mp4', 17)
# video.run(VideoViewer.MODE_OUTPUT)

# VIDEO SAMPLES - DAY 2

# video = VideoViewer('resource/video_samples/input/teste_controlado_50_day2.mp4', 1)
# video.run(VideoViewer.MODE_OUTPUT)

# video = VideoViewer('resource/video_samples/input/teste_controlado_60_day2.mp4', 30)
# video.run(VideoViewer.MODE_OUTPUT)

# video = VideoViewer('resource/video_samples/input/teste_controlado_80_day2.mp4', 27)
# video.run(VideoViewer.MODE_OUTPUT)

# video = VideoViewer('resource/video_samples/input/teste_controlado_100_day2.mp4', 33)
# video.run(VideoViewer.MODE_OUTPUT)
