import yt_dlp
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FFMPEG_PATH = os.path.abspath(os.path.join(BASE_DIR, "..", "bin"))

def telecharger_mp3(url, dossier_utilisateur):
    try :
        options = {
            "ffmpeg_location": FFMPEG_PATH,
            "format" :  "bestaudio/best",
            "outtmpl" : os.path.join(dossier_utilisateur, "%(title)s.%(ext)s"),
            "postprocessors" : [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }
            ]
        }
        with yt_dlp.YoutubeDL(options) as ydl:
            ydl.download([url])
        return True
    except Exception as e:
        print(f"Le téléchargement a planté : {e}")
        return False