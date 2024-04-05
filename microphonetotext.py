from faster_whisper import WhisperModel

import gradio as gr



def microphonettext(input,model):
    seg = " "
    segments, info = model.transcribe((input))
    for segment in segments:
        seg += "%s" % (segment.text)
    return seg

