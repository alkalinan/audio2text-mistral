import os
import sys
import requests
import tempfile
from moviepy.editor import AudioFileClip

def split_audio(file_path, segment_length_sec=15*60):
    audio = AudioFileClip(file_path)
    duration_sec = int(audio.duration)
    segments = []
    base_name = os.path.splitext(os.path.basename(file_path))[0]
    for i in range(0, duration_sec, segment_length_sec):
        start = i
        end = min(i + segment_length_sec, duration_sec)
        segment_file = tempfile.NamedTemporaryFile(delete=False, suffix='.mp3')
        segment = audio.subclip(start, end)
        segment.write_audiofile(segment_file.name, codec='mp3')
        segments.append(segment_file.name)
    audio.close()
    return segments

import json

def transcribe_audio(file_path, api_key, model="voxtral-mini-2507", language="fr"):
    url = "https://api.mistral.ai/v1/audio/transcriptions"
    headers = {
        "x-api-key": api_key
    }
    files = {
        "file": open(file_path, "rb"),
        "model": (None, model),
        "language": (None, language)
    }
    response = requests.post(url, headers=headers, files=files)
    files["file"].close()
    if response.status_code == 200:
        try:
            data = response.json()
            return data.get("text", "")
        except Exception as e:
            print(f"Erreur de parsing JSON: {e}")
            return ""
    else:
        print(f"Erreur API: {response.status_code} - {response.text}")
        return ""

def main():
    if len(sys.argv) < 3:
        print("Usage: python audio2text.py <audio_file> <api_key>")
        sys.exit(1)
    audio_file = sys.argv[1]
    api_key = sys.argv[2]
    segments = split_audio(audio_file)
    full_text = ""
    for seg in segments:
        print(f"Transcription du segment: {seg}")
        text = transcribe_audio(seg, api_key)
        full_text += text + "\n"
        os.remove(seg)
    output_file = os.path.splitext(audio_file)[0] + "_transcript.txt"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(full_text)
    print(f"Transcription terminée: {output_file}")

if __name__ == "__main__":
    main()
