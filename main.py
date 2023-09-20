from pytube import Playlist,YouTube
import os
import diretorios_util
base_link= "https://www.youtube.com/watch?v=asSnpF6vJAI"
p = Playlist(base_link)
print("INICIO DOWNLOAD")
diretorios_util.create_dirs(diretorios_util.get_download_mp4_dir())
diretorios_util.dirs_exists_or_throw_runtime(diretorios_util.get_download_mp4_dir())
##caso seja uma playlist
try:
    print(f"A PLAYLIST TEM {len(p.video_urls)} VIDEOS")
    for url in p.video_urls[:3]:
        print(url)
except KeyError:
    print("VIDEO UNICO, BAIXANDO")
    yt = YouTube(base_link)
    best_resolution_mp4 = yt.streams.filter(file_extension='mp4').get_highest_resolution()
    print(f"CAMINHO DO DOWNLOAD {diretorios_util.get_download_mp4_dir()}")
    best_resolution_mp4.download(diretorios_util.get_download_mp4_dir())
except:
    print("UM ERRO INESPERADO OCORREU NO PROGRAMA!!")

#caso nao seja
