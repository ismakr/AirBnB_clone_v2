#!/usr/bin/python3
"""distributes an archive to the web servers"""
from fabric.api import *
env.hosts = ['100.25.45.81', '100.26.227.36']


def do_deploy(archive_path):
    """distributes an archive to the web servers"""
    try:
        put(archive_path, "/tmp/")
        archive_dir = archive_path.split('.')[0].split('/')[1]
        archive_dir_path = f"/data/web_static/releases/{archive_dir}/"
        tmp_archive_file = "/tmp/" + archive_path.split('/')[1]
        run(f"mkdir -p {archive_dir_path}")
        run(f"tar -xzf {tmp_archive_file} -C {archive_dir_path}")
        run(f"rm {tmp_archive_file}")
        run(f"mv {archive_dir_path}web_static/* {archive_dir_path}")
        run(f"rm -rf {archive_dir_path}web_static/")
        run(f"rm rf /data/web_static/current")
        run(f"ln -s {archive_dir_path} /data/web_static/current")
        return True
    except():
        return False
