import subprocess, os, apt, errno, requests
# This requires python-apt be installed, apt-get install python-apt

def install_dep():
    cache = apt.Cache()
    cache.open()
    dep = ['mailutils', 'postfix', 'curl', 'wget', 'file', 'bzip2', 'gzip', 'unzip', 'bsdmainutils', 'util-linux', 'ca-certificates', 'tmux', 'lib32gcc1', 'libstdc++6', 'libstdc++6:i386']
    subprocess.call(["dpkg", "--add-architecture", "i386"])
    subprocess.call(["apt-get", "update"])
    for item in dep:
        try:
            response = "package "+item+" Installed"
            cache[item].is_installed
            print(response)
        except KeyError:
            response = "Package is not Installed, Installing now"
            print(response)
            subprocess.call(["apt-get", "install", item]);

def get_steam():
    try:
        os.makedirs('/DragonSoft/steamcmd')
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise
    file_url = "https://steamcdn-a.akamaihd.net/client/installer/steamcmd_linux.tar.gz"
    r = requests.get(file_url, stream = True)
    with open("steamcmd_linux.tar.gz", "wb") as tar:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                tar.write(chunk)
    subprocess.call(["mv", "steamcmd_linux.tar.gz", "/DragonSoft/steamcmd/steamcmd_linux.tar.gz"])
    subprocess.call(["tar", "zxvf", "/DragonSoft/steamcmd/steamcmd_linux.tar.gz", "-C", "/DragonSoft/steamcmd/"])
    subprocess.call(["/DragonSoft/steamcmd/steamcmd.sh", "+login", "anonymous", "+quit"])
    subprocess.call(["chmod", "-R", "777", "/DragonSoft"]);
