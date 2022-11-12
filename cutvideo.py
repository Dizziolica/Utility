from moviepy.editor import *

clip = VideoFileClip('/home/dizziolica/Music/Steven/steven.mp4')

clip = clip.subclip(80, 100)

clip.write_videofile('/home/dizziolica/Music/Steven/test.mp4')