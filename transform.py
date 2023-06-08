# way 1 video part to audio part
from moviepy.editor import AudioFileClip
my_audio_clip = AudioFileClip("e:/chrome/my_video.mp4")
my_audio_clip.write_audiofile("e:/chrome/my_audio.wav")


# way 2
import moviepy.editor as mp

def extract_audio(videos_file_path):
    my_clip = mp.VideoFileClip(videos_file_path)

extract_audio('C:\my_videos\abc.mp4')

my_clip.audio.write_audiofile(f'{videos_file_path}.mp3')

import moviepy.editor as mp
def extract_audio(videos_file_path):
    my_clip = mp.VideoFileClip(videos_file_path)
    my_clip.audio.write_audiofile(f'{videos_file_path}.mp3')