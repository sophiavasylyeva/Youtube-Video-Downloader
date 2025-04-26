from sys import argv
import yt_dlp

link = argv[1]
ydl_opts = {
    'outtmpl': 'C:/Users/sophi/Downloaded Youtube Videos/%(title)s.%(ext)s'
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(link)  
    print("Title:", info.get('title'))
    

