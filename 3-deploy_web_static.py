#!/usr/bin/python3
"""creates and distributes an archive to your web servers,
using the function deploy"""
from fabric.api import *
from os.path import exists
env.hosts = ['100.25.45.81', '100.26.227.36']


def do_pack():
    """generates a .tgz archive from the contents of the web_static"""
    local('sudo mkdir -p versions')
    foltime = datetime.now().strftime('%Y%m%d%H%M%S')
    fl = f"versions/web_static_{foltime}.tgz"
    com = local(f"sudo tar -cvzf {fl} web_static")
    if com.succeeded:
        return fl
    else:
        return None


def do_deploy(archive_path):
    """distributes an archive to the web servers"""
    if exists(archive_path) is False:
        return False
    try:
        archive_dir = f"{archive_path.split('.')[0].split('/')[1]}"
        archive_dir_path = f"/data/web_static/releases/{archive_dir}"
        tmp_archive_file = "/tmp/" + f"{archive_path.split('/')[1]}"
        put(archive_path, "/tmp/")
        run(f"sudo mkdir -p {archive_dir_path}/")
        run(f"sudo tar -xzf {tmp_archive_file} -C {archive_dir_path}/")
        run(f"sudo rm {tmp_archive_file}")
        run(f"sudo mv {archive_dir_path}/web_static/* {archive_dir_path}/")
        run(f"sudo rm -rf {archive_dir_path}/web_static")
        run(f"sudo rm -rf /data/web_static/current")
        run(f"sudo ln -s {archive_dir_path}/ /data/web_static/current")
        return True
    except():
        return False


def deploy(archive_path):
    """creates and distributes an archive to the web servers"""
    arch = do_pack()
    if exists(new_archive_path) is False:
        return False
    res = do_deploy(arch)
    return res
