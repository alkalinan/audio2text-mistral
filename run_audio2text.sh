#!/bin/zsh
# Script pour créer un environnement virtuel Python 3.13, installer les dépendances et lancer le script audio2text

# Chemin du fichier audio et clé API à adapter
AUDIO_FILE="$1"
API_KEY="$2"

if [ -z "$AUDIO_FILE" ] || [ -z "$API_KEY" ]; then
  echo "Usage: ./run_audio2text.sh <chemin_fichier_audio> <api_key>"
  exit 1
fi

# Crée l'environnement virtuel si non existant
if [ ! -d ".venv" ]; then
  python3 -m venv .venv
fi

# Active l'environnement virtuel
source .venv/bin/activate

# Installe les dépendances compatibles Python 3.13
pip install -r requirements-py313.txt

# Lance le script principal
python audio2text.py "$AUDIO_FILE" "$API_KEY"

# Désactive l'environnement virtuel
deactivate
