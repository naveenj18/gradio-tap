from faster_whisper import WhisperModel
import gradio as gr

final=[]

def audiototranslate(input,model):
   seg=" "
   segments, info = model.transcribe((input),language="en")
   for segment in segments:
     seg +="%s" % (segment.text)
   return seg

