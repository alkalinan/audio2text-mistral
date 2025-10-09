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
- `<chemin_fichier_audio>` : chemin vers le fichier audio à transcrire (MP4, MP3, WAV...)
- `<votre_api_key>` : clé API Mistral

Le script :
1. Découpe l’audio en segments de 15 minutes maximum.
2. Transcrit chaque segment via l’API Mistral.
3. Regroupe les textes dans un fichier `<nom_audio>_transcript.txt`.

## Exemple

```sh
python audio2text.py entretien_KARPOWICZ_Nicolas.mp4 68D6fIPfoq9RRzvJbSQddPCesHMXpA8Z
```

## Configuration du projet

Le projet utilise `pyproject.toml` (Poetry) et `requirements.txt` pour la gestion des dépendances. Compatible avec pyenv, pip et poetry.

---

N’hésite pas à adapter le script ou la configuration selon tes besoins !
