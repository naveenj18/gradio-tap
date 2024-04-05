from faster_whisper import WhisperModel
import gradio as gr
from pytube import YouTube
from moviepy.editor import AudioFileClip,VideoFileClip
from audiototext import audiototext
from videototext import videototext
from microphonetotext import microphonettext 
from  streamtotext import streamtotext
from ytotext import yt_to_audio
from audiototrans import audiototranslate
from texttospeech import texttospeech
from timestamped import timestamp
import whisper_timestamped as whisper

model = WhisperModel("large-v2") 
def tab1(input):
  return audiototext(input,model)
def tab2(input):
  return videototext(input,model)
def tab3(input):
  return microphonettext(input,model)
def tab4(input):
  return streamtotext(input,model)
def tab5(input):
  return yt_to_audio(input,model)
def tab6(input):
  return audiototranslate(input,model)
def tab7(input):
  return timestamp(input)
with gr.Blocks() as naveen:
    with gr.Tab("audiofile to transcribe"):
      gr.Interface(fn=tab1,inputs=[gr.Audio(sources="upload",type="filepath")],outputs="text",examples=[["A-J-Cook-Speech (1).mp3"],["g.mp3"]]
                   ,title="Audio to text",description="tell something to whisper")
    with gr.Tab("video file to transcription"):
       gr.Interface(fn=tab2,inputs=gr.Video(),outputs="text",examples=[["v1.mp4"],["dhoni.mp4"]],title="Video to text Converter",description="Extract audio from a video file and play it in the Gradio UI.")
    with gr.Tab("microphone to transcription"):
      gr.Interface(fn=tab3,inputs=[gr.Audio(sources="microphone",type="filepath")],outputs="text",title="Microphone to Transcription",description="tell something to whisper")
    
    
    with gr.Tab("live audio streaming to transcription"):
      gr.Interface(fn=tab4,inputs=[gr.Audio(type="filepath",streaming=True)],outputs="text",title="Live Audio streaming to transcription",description="tell something to whisper",live=True)
    
    with gr.Tab("yt link to transcription"):
      gr.Interface(fn=tab5,inputs=["textbox"],outputs="text",examples=[["https://www.youtube.com/watch?v=ekZZZPRxWtI"],["https://www.youtube.com/watch?v=pJY0mBWHPw4"],],title="Youtube Link to transcription",
    description="Extract audio from a video file and play it in the Gradio UI.")
    
    with gr.Tab("translate"):
      gr.Interface(fn=tab6,inputs=gr.Audio(type="filepath"),outputs="text",title="Translate",examples=[["hindi.mp3"],["tamil.mp3"]],)
      
    with gr.Tab("text to speech"):
      gr.Interface(fn=texttospeech,inputs="text",outputs="audio",examples=[["Wake up to reality nothing ever goes as planned in this world "],["what happend to you"]],title="speech to text",description="naveen enter text then it convert into audio")

    with gr.Tab("Timestaming"):
      gr.Interface(fn=timestamp,inputs=[gr.Audio(type="filepath")],outputs="text",title="timestamping",)




naveen.launch(share=True)