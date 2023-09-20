from pytube import YouTube
class youtube_download:
    
    @staticmethod
    def download_single_video(url,base_dir):
        yt = YouTube(url)
        print(f"BAIXANDO {yt.title}: ")
        best_resolution_mp4 = yt.streams.filter(file_extension='mp4').get_highest_resolution()
        print(f"CAMINHO DO DOWNLOAD {base_dir}")
        best_resolution_mp4.download(base_dir)

    @staticmethod
    def download_playlist(playlist,base_dir):
        for url in playlist.video_urls:
            youtube_download.download_single_video(url,base_dir)
    