#!/bin/zsh
# Script pour extraire l'audio d'une vidéo avec Python et moviepy

VIDEO_FILE="$1"
OUTPUT_AUDIO="$2"

if [ -z "$VIDEO_FILE" ]; then
  echo "Usage: ./run_video2audio.sh <chemin_video> [chemin_audio_sortie]"
  exit 1
fi

# Crée l'environnement virtuel si non existant
if [ ! -d ".venv" ]; then
  python3 -m venv .venv
fi

# Active l'environnement virtuel
source .venv/bin/activate

# Installe les dépendances nécessaires
pip install moviepy

# Si OUTPUT_AUDIO n'est pas donné, le génère automatiquement
if [ -z "$OUTPUT_AUDIO" ]; then
  BASENAME=$(basename "$VIDEO_FILE")
  BASENAME_NOEXT="${BASENAME%.*}"
  DIRNAME=$(dirname "$VIDEO_FILE")
  OUTPUT_AUDIO="$DIRNAME/$BASENAME_NOEXT.mp3"
fi

# Lance le script Python
python video2audio.py "$VIDEO_FILE" "$OUTPUT_AUDIO"

# Désactive l'environnement virtuel
deactivate
