#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive
from the contents of the web_static
"""
from fabric.api import local
from datetime import datetime

def do_pack():
    """
    Generate a .tgz archive from the contents of the web_static folder.
    """
    local("mkdir -p versions")

    time = datetime.now()
    str_time = time.strftime("%Y%m%d%H%M%S")


    archive = "web_static_{}.tgz".format(str_time)
    output = local("tar -cvzf versions/{} web_static".format(archive))

    if output is not None:
        return "versions/" + archive
    else:
        return None
