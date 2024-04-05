from transformers import Wav2Vec2ForCTC, Wav2Vec2Tokenizer
import soundfile as sf
import torch
import gradio as gr

tokenizer = Wav2Vec2Tokenizer.from_pretrained("facebook/wav2vec2-large-960h")
model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-large-960h")

def transcribe_audio(input_audio):
    audio_input, _ = sf.read(input_audio.name)
    input_values = tokenizer(audio_input, return_tensors="pt").input_values
    with torch.no_grad():
        logits = model(input_values).logits
    predicted_ids = torch.argmax(logits, dim=-1)
    transcription = tokenizer.batch_decode(predicted_ids)[0]

    return transcription
audio_input = gr.Audio(source="microphone", type="microphone")
output_text = gr.Textbox(label="Transcription")
gr.Interface(fn=transcribe_audio, inputs=audio_input, outputs=output_text).launch()
