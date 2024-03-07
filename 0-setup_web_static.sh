#!/usr/bin/env bash
#setting up the server

folder1='/data/'
folder2='/data/web_static/'
folder3='/data/web_static/releases/'
folder4='/data/web_static/shared/'
folder5='/data/web_static/releases/test/'
file='/data/web_static/releases/test/index.html'

symbolic_link_path='/data/web_static/current'
symbolic_link_target='/data/web_static/releases/test/'

#function to create directories
create_directory() {
    if [ ! -d "$1" ];
    then
        mkdir -p "$1"
    fi
}

#function to create symbolic links
create_symbolic_link() {
    ln -s -f "$1" "$2"
}

#create directories
create_directory "$folder1"
create_directory "$folder2"
create_directory "$folder3"
create_directory "$folder4"
create_directory "$folder5"

#creating a fake html file
echo "
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee "$file"

#creating a symbolic link
create_symbolic_link "$symbolic_link_target" "$symbolic_link_path"

#giving ownership of /data/ to user and group ubuntu
sudo chown -R ubuntu:ubuntu /data/

#updating nginx configuration 
sudo sed -i '/listen 80 default_server;/a location /hbnb_static {alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default

#restarting nginx
sudo service nginx restart
