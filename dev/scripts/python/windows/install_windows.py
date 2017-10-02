import os, subprocess, errno, urllib, zipfile
from urllib import request

def get_steam():

    steam_dir = "C:\DragonSoft\steamcmd\\"
    steam_dir_file = "C:\DragonSoft\steamcmd\steamcmd.zip"
    
    try:
        os.makedirs(steam_dir)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise
    file_url = "https://steamcdn-a.akamaihd.net/client/installer/steamcmd.zip"
    urllib.request.urlretrieve(file_url, steam_dir_file)
    with zipfile.ZipFile(steam_dir_file, 'r') as zip_ref:
        zip_ref.extractall(steam_dir)
        subprocess.call(["C:\DragonSoft\steamcmd\steamcmd", "+login", "anonymous", "+quit"]) 
