import yt_dlp


link = "https://youtu.be/ehfLnF5p8i0?si=cPdu8f_DbWw9mNRu"

formato_salida = "mp3"
calidad = "192"

ydl_opts = {
        "format": "bestaudio/best",
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": formato_salida,
            "preferredquality": calidad, 
            }],
            "outtmpl": "%(title)s.%(ext)s",
        }

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([link])
