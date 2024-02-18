from pytube import YouTube,Playlist
import os
from converter import convert_mp4_to_mp3, removeExtensionMP4
import diretorios_util
import arquivo_util
import os.path
from pathlib import Path,PurePosixPath
class youtube_download:
    
    @staticmethod
    def download_single_video(url,base_dir):
        yt = YouTube(url)
        print(f"BAIXANDO {yt.title} ")
        index = -1
        
        tentativa = 0
        baixado = False
        while(not baixado and tentativa<3):
            try:
                best_resolution_mp4 = yt.streams.filter(mime_type="video/mp4",progressive=True).asc()[index]
                print(f"BAIXANDO RESOLUCAO {best_resolution_mp4.resolution} | {best_resolution_mp4.title} ")
                video_baixado = best_resolution_mp4.download(base_dir)
                baixado = True
                return video_baixado

            except Exception as e:
                print(e)
                print("DEU ERRO")
                index+=1
            finally:
                tentativa+=1
        
        raise Exception("falha ao baixar o video!!!")

    @staticmethod
    def download_playlist(playlist,diretorio_mp4,diretorio_mp3):
        downloaded = {}
        for url in playlist.video_urls:
            print(url)
            try:
                arquivo_video = youtube_download.download_single_video(url,diretorio_mp4)
            # print(diretorios_util.check_if_dirs_exists(youtube_download.download_single_video(url,base_dir)))
                print(f"MP3 SEM EXTENSAO '{removeExtensionMP4(arquivo_video)}'")
                mp3_name = PurePosixPath(removeExtensionMP4(arquivo_video)).name
                print(f"MP3 NAME '{mp3_name}'")
                caminho_arquivo_mp3 = os.path.join(diretorio_mp3,mp3_name)
                print(f"ARQUIVO VIDEO{arquivo_video}")
                convert_mp4_to_mp3(arquivo_video,caminho_arquivo_mp3)
                diretorios_util.delete_file(arquivo_video)
                downloaded[url] = "BAIXADO"
            except Exception as e:
                print(e)
                downloaded[url] = "ERRO"

        
    #return a list of mp4 videos
# url ="https://www.youtube.com/playlist?list=PLeikwWbUYhhBKOukahZX7OJ1F8qHS3XDQ" patricia
url = "https://www.youtube.com/playlist?list=PLOEWJragbGr3H5-36SLkcsAFpaPZ2entR"
# url = "https://www.youtube.com/playlist?list=PLOEWJragbGr26oR4SpQso8xNxe5Kf68rY"

# url = "https://www.youtube.com/playlist?list=PLOEWJragbGr0bgUp0_Lj9R6yUROFN3ELI"
downloaded_videos = youtube_download.download_playlist(Playlist(url),"./mp4","./mp3")
print(downloaded_videos)
