from moviepy.editor import *


class MovieTool:

    def __init__(self):
        pass

    @staticmethod
    def save_mp4_to_gif(origin_file, convert_file):
        clip = VideoFileClip(origin_file)
        duration = clip.duration
        if duration > 10:
            clip.subclip(0, 10)
        else:
            clip = clip.subclip(0, int(duration))
        clip.write_gif(convert_file)