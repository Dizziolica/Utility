def cutvideo(start, end, path1, path2):

    from moviepy.editor import *

    clip = VideoFileClip(path1)

    clip = clip.subclip(start, end)

    clip.write_videofile(path2)
