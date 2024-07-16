#!/usr/bin/python3
"""
Fabric script (based on the file 1-pack_web_static.py) that distributes
an archive to your web servers, using the function do_deploy
"""

from fabric.api import put, run, env
from os.path import exists
env.hosts = ['52.3.246.208', '52.86.211.25']


def do_deploy(archive_path):
    """ distributes an archive to your web servers"""
    if exists(archive_path) is False:
        return False
    try:
        file_no = archive_path.split("/")[-1]
        no_exts = file_n.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, no_exts))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_no, path, no_exts))
        run('rm /tmp/{}'.format(file_n))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_exts))
        run('rm -rf {}{}/web_static'.format(path, no_exts))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_exts))
        return True
    except:
        return False
