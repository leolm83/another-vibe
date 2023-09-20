from pytube import Playlist
import traceback
import diretorios_util
from youtube_downloader import youtube_download
base_link= "https://www.youtube.com/watch?v=9iJ6hoosGRU&list=PLOEWJragbGr2l5A-uG-WroCI_-pC_dtSB"
base_dir = diretorios_util.get_download_mp4_dir()

playlist = Playlist(base_link)
print("INICIO DOWNLOAD")
diretorios_util.create_dirs(base_dir)
diretorios_util.dirs_exists_or_throw_runtime(base_dir)
##caso seja uma playlist
try:
    print(f"A PLAYLIST TEM {len(playlist.video_urls)} VIDEOS")
    youtube_download.download_playlist(playlist,base_dir)
    print("DOWNLOAD DA PLAYLIST CONCLUIDO")
except KeyError:
    print("VIDEO UNICO, BAIXANDO")
    youtube_download.download_single_video(base_link,base_dir)
    print("DOWNLOAD CONCLUIDO")
except Exception as e:
    print(traceback.format_exc())
    print("UM ERRO INESPERADO OCORREU NO PROGRAMA!!")

#caso nao seja
