from faster_whisper import WhisperModel



def audiototext(input,model):
    seg = " "
    segments, info = model.transcribe(input)
    for segment in segments:
        seg += "%s" % (segment.text)
    return seg

