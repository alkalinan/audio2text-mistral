# audio2text-mistral

Script Python pour transformer un fichier audio (MP4, MP3, WAV...) en texte via l’API Mistral, avec découpage automatique en segments de 15 minutes maximum.

## Prérequis

- Python 3.8+
- ffmpeg installé sur le système (utilisé par pydub)
- Dépendances Python :
  - pydub



Installation des dépendances :

```sh

pip install -r requirements.txt
```

## Installation de ffmpeg
- macOS :
  ```sh
  brew install ffmpeg

  ```

- Ubuntu/Debian :

  ```sh
  sudo apt-get install ffmpeg
  ```
- Windows :
  Télécharger sur https://ffmpeg.org/download.html et ajouter à votre PATH.



## Utilisation

```sh
python audio2text.py <chemin_fichier_audio> <votre_api_key>
```

## Extraction de l'audio depuis une vidéo

Pour extraire l'audio d'une vidéo (MP4, MOV, etc.) :

### Commandes pour lancer le script bash

```sh
chmod +x run_video2audio.sh
./run_video2audio.sh <chemin_video> [chemin_audio_sortie]
```
- `<chemin_video>` : chemin vers le fichier vidéo
- `[chemin_audio_sortie]` : (optionnel) chemin du fichier audio MP3 à générer

Le script crée un environnement virtuel, installe moviepy et extrait l'audio en MP3 via le script Python `video2audio.py`.
Si le chemin de sortie n'est pas donné, le fichier audio est créé dans le même dossier que la vidéo, avec le même nom et l'extension `.mp3`.

---

## Transcription audio en texte

### Commandes pour lancer le script bash

```sh
chmod +x run_audio2text.sh
./run_audio2text.sh <chemin_fichier_audio> <votre_api_key>
```
- `<chemin_fichier_audio>` : chemin vers le fichier audio à transcrire (MP3, WAV, MP4...)
- `<votre_api_key>` : clé API Mistral

Le script découpe l'audio en segments, les transcrit via l'API Mistral et regroupe le texte dans un fichier.
Le script :
1. Découpe l’audio en segments de 15 minutes maximum.
2. Transcrit chaque segment via l’API Mistral.
3. Regroupe les textes dans un fichier `<nom_audio>_transcript.txt`.

```sh
python audio2text.py path/to/audio-file.mp4 MISTRAL-API-KEY
```

## Configuration du projet

Le projet utilise `pyproject.toml` (Poetry) et `requirements.txt` pour la gestion des dépendances. Compatible avec pyenv, pip et poetry.

---

N’hésite pas à adapter le script ou la configuration selon tes besoins !
