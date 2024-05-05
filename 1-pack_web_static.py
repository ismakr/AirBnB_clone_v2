#!/usr/bin/python3
""" generates a .tgz archive from the contents of the web_static"""
from fabric.api import *
from datetime import datetime


def do_pack():
    """generates a .tgz archive from the contents of the web_static"""
    local('sudo mkdir -p versions')
    foltime = datetime.now().strftime('%Y%m%d%H%M%S')
    fl = "versions/web_static_{foltime}.tgz"
    com = local('ftar -cvzf {fl} web_static')
    if com.succeeded:
        return fl
    else:
        return None
