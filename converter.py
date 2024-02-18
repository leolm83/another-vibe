from moviepy.editor import *
from diretorios_util import delete_file

def convert_mp4_to_mp3(video,arquivo_destino_mp3):
 
    try:
        videoclip = VideoFileClip(video)
        audioclip = videoclip.audio
        # print(video)
        audioclip.write_audiofile(arquivo_destino_mp3)
        # print(arquivo_destino_mp3)
        audioclip.close()
        videoclip.close()
    ## todo implement this
        return arquivo_destino_mp3
    except Exception as e:
        delete_file(arquivo_destino_mp3)
        raise e
        
def removeExtensionMP4(video):
    return video.replace("mp4","mp3")
