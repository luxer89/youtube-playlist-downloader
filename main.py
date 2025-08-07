import os
from yt_dlp import YoutubeDL


PLAYLIST_URL = "https://www.youtube.com/playlist?list=PL_YLeKdeI1Y1KfJCEqSjddBLYA2ko2WB" 


OUTPUT_FOLDER = "downloads" # Створює дерикторію з назвою downloads


os.makedirs(OUTPUT_FOLDER, exist_ok=True)


ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': f'{OUTPUT_FOLDER}/%(playlist_index)03d - %(title)s.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'yesplaylist': True,
    'noplaylist': False,
    'quiet': False
}


with YoutubeDL(ydl_opts) as ydl:
    print("⬇️ Починаємо завантаження плейлиста...")
    ydl.download([""]) # Посилання до плейлиста
    print("Увесь плейлист завантажено та конвертовано у MP3!")
