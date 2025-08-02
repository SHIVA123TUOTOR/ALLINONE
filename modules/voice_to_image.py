import requests
import os
import time
import sounddevice as sd
from scipy.io.wavfile import write
from modules.image_generator import generate_image_from_text

def voice_to_image():
    fs = 44100
    duration = 5
    print("Recording for 5 seconds...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    write("audio/prompt.wav", fs, recording)
    print("Saved audio/prompt.wav")

    print("Sending to AssemblyAI for transcription...")
    upload_url = "https://api.assemblyai.com/v2/upload"
    headers = {"authorization": "assemblyai-e238350da8ad4b7f8c077731ff80c8f8"}
    with open("audio/prompt.wav", "rb") as f:
        response = requests.post(upload_url, headers=headers, files={"file": f})
    audio_url = response.json()["upload_url"]

    transcribe_url = "https://api.assemblyai.com/v2/transcript"
    json_data = {"audio_url": audio_url}
    response = requests.post(transcribe_url, json=json_data, headers=headers)
    transcript_id = response.json()["id"]

    while True:
        poll = requests.get(f"https://api.assemblyai.com/v2/transcript/{transcript_id}", headers=headers)
        status = poll.json()["status"]
        if status == "completed":
            prompt = poll.json()["text"]
            print("Prompt:", prompt)
            generate_image_from_text(prompt)
            break
        elif status == "failed":
            print("Transcription failed")
            break
        time.sleep(3)
