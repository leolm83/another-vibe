import os

# get the current working directory
nome_pasta_download = "mp4"

def get_current_dir():
    return os.getcwd()

def get_download_mp4_dir():
    return os.path.join(get_current_dir(),nome_pasta_download)

def check_if_dirs_exists(path):
    return os.path.exists(path)

def create_dirs(path):
    if(not check_if_dirs_exists(path)):
        os.makedirs(path)
def  dirs_exists_or_throw_runtime(path):
    if(not check_if_dirs_exists(path)):
        raise FileNotFoundError(f"FILE NAO EXISTE : ${path}")
    
def delete_file(file):
    if(check_if_dirs_exists(file)):
        os.remove(file)