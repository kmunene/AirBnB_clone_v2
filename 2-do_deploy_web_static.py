#!/usr/bin/python3
"""Fabric script to distribute an archive to web servers"""

from fabric.api import env, put, run
from os.path import exists
from datetime import datetime

env.hosts = ['ubuntu@54.152.135.240', 'ubuntu@34.224.4.197']
env.key_filename = "~/.ssh/school"


def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:

        put(archive_path, '/tmp/')

        archive_filename = archive_path.split("/")[-1]
        archive_no_ext = archive_filename.split(".")[0]
        release_path = '/data/web_static/releases/{}'.format(archive_no_ext)

        run('mkdir -p {}'.format(release_path))
        run('tar -xzf /tmp/{} -C {}'.format(archive_filename, release_path))

        run('rm /tmp/{}'.format(archive_filename))

        run('rm -f /data/web_static/current')

        run('ln -s {} /data/web_static/current'.format(release_path))

        return True

    except Exception as e:
        return False
