# youtube-playlist-downloader
Ця програма завантужує ваш ютуб плейлист та перетвоює у формат .mp3

        Перед використанням, вам потрібно завантажити:

        1. yt-dlp
        2. ffmpeg
---

## yt-dlp є два варіанта для завантаження

- Прописуєте цю команду в консоль
``` bash
pip install -U yt-dlp
```

- Або вручну якщо у вас Linux Ubuntu/Debian:

```bash
sudo curl -L https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp -o /usr/local/bin/yt-dlp
sudo chmod a+rx /usr/local/bin/yt-dlp

```

## для ffmpeg
``` bash
sudo apt update
sudo apt install ffmpeg
```
- або для windows 
Завантажуєте з цього сайту https://ffmpeg.org/download.html і додайте до ```PATH```

----

# Запуск коду виконується через команду 
``` bash
python3 main.py
```

__Якщо вам треба файл в іншому форматі (наприклад у WAV формат), просто поміняйте у коді значення mp3 на WAV__

```python
'preferredcodec': 'mp3',
```

__На:__
```python
'preferredcodec': 'wah',
```

дякую