import sys
import os
from moviepy.editor import VideoFileClip

def extract_audio(video_path, output_audio_path=None):
    if not os.path.isfile(video_path):
        print(f"Fichier vidéo introuvable: {video_path}")
        sys.exit(1)
    if output_audio_path is None:
        base, _ = os.path.splitext(video_path)
        output_audio_path = base + ".mp3"
    clip = VideoFileClip(video_path)
    clip.audio.write_audiofile(output_audio_path, codec='mp3')
    clip.close()
    print(f"Audio extrait: {output_audio_path}")
    return output_audio_path

def main():
    if len(sys.argv) < 2:
        print("Usage: python video2audio.py <chemin_video> [chemin_audio_sortie]")
        sys.exit(1)
    video_path = sys.argv[1]
    output_audio_path = sys.argv[2] if len(sys.argv) > 2 else None
    extract_audio(video_path, output_audio_path)

if __name__ == "__main__":
    main()
