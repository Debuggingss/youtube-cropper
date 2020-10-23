from moviepy.editor import *
import pytube

# Settings #
URL = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
FILENAME = 'dl'
START_TIME = 0
END_TIME = 10
FPS = 15
# -------- #


def download_video(url, filename):
    """
    :param url: Define YouTube URL
    :param filename: Set a file name for the video
    """
    youtube = pytube.YouTube(url)
    video = youtube.streams.first()
    video.download(filename=f"{filename}_ORIGINAL")


class YoutubeCropper:
    def __init__(self, filename):
        self.filename = filename

    def cut_video(self, start, end, fps):
        """
        :param start: Set start timestamp
        :param end: Set end timestamp
        :param fps: Set frames per second
        :return:
        """
        vid = VideoFileClip(f"{self.filename}_ORIGINAL.mp4")
        clip = vid.subclip(start, end)
        clip.write_videofile(f"{self.filename}.mp4", fps=fps)
        return

    def convert_to_mp3(self):
        """
        :return:
        """
        vid = VideoFileClip(f"{self.filename}_ORIGINAL.mp4")
        audio = vid.audio
        audio.write_audiofile(f"{self.filename}_FULL.mp3")
        return

    def cut_to_mp3(self, start, end):
        """
        :param start: Set start timestamp
        :param end: Set end timestamp
        :return:
        """
        vid = VideoFileClip(f"{self.filename}_ORIGINAL.mp4")
        clip = vid.subclip(start, end)
        audio = clip.audio
        audio.write_audiofile(f"{self.filename}.mp3")
        return

    def cut_to_gif(self, start, end, fps):
        """
        :param start: Set start timestamp
        :param end: Set end timestamp
        :param fps: Set GIF frames per second
        :return:
        """
        vid = VideoFileClip(f"{self.filename}_ORIGINAL.mp4")
        clip = vid.subclip(start, end)
        clip.write_gif(f"{self.filename}.gif", fps=fps)
        return


if __name__ == '__main__':
    # Download the video
    download_video(URL, FILENAME)

    # Cut the video
    YoutubeCropper(FILENAME).cut_video(START_TIME, END_TIME, FPS)

    # Convert the ORIGINAL video to mp3 without timestamps
    YoutubeCropper(FILENAME).convert_to_mp3()

    # Cut the ORIGINAL video to mp3 format using our timestamps
    YoutubeCropper(FILENAME).cut_to_mp3(START_TIME, END_TIME)

    # Cut the ORIGINAL video to gif format using our timestamps
    YoutubeCropper(FILENAME).cut_to_gif(START_TIME, END_TIME, 10)
