import whisper_timestamped as whisper
model = whisper.load_model("tiny")
def timestamp (input):
    audio = whisper.load_audio(input)
    result = whisper.transcribe(model, audio, language="en")
    import json
    final=json.dumps(result, indent = 2, ensure_ascii = False)
    return final