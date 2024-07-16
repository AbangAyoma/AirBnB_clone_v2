#!/usr/bin/python3
"""
Fabric script (based on the file 2-do_deploy_web_static.py) that creates
and distributes an archive to your web servers
"""

from datetime import datetime
from fabric.api import *
env.hosts = ['52.3.246.208', '52.86.211.25']
from os.path import exists, isdir
from datetime import datetime
from fabric.api import env, local, put, run


def do_pack():
    """
    makes an archive on web static folder
    """

    time = datetime.now()
    archive = 'web_static_' + time.strftime("%Y%m%d%H%M%S") + '.' + 'tgz'
    local('mkdir -p versions')
    create = local('tar -cvzf versions/{} web_static'.format(archive))
    if create is not None:
        return archive
    else:
        return None


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


def deploy():
    """ creates and distributes an archive to your web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
