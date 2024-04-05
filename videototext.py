from faster_whisper import WhisperModel
import gradio as gr
from moviepy.editor import AudioFileClip,VideoFileClip




def videototext(video_path,model):
    video = VideoFileClip(video_path)
    audio = video.audio
    audio_path = "extracted_audio." + ".mp3"
    audio.write_audiofile(audio_path)
    video.close()
    seg=" "
    segments, info = model.transcribe((audio_path))
    for segment in segments:
      seg +="%s" % (segment.text)
    return seg