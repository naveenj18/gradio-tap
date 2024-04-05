from TTS.api import TTS
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2")
def texttospeech(input):
    output=tts.tts_to_file(text=input,
                file_path="output.wav",
                speaker_wav=["/home/team2/naveen/tab/extracted_audio..mp3"],
                language="en",
                split_sentences=True
                )
    return output