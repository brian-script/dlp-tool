import yt_dlp

link = input("Ingresa el link del video: ")

print("quieres descargar el video o solo el audio?: \n1- video(mp4)\n2- audio(mp3)")
opcion = int(input("elige una opcion: "))

if opcion == 1:
    ydl_opts = {
            "format": "best",}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])

elif opcion == 2:
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
