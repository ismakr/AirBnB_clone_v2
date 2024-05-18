#!/usr/bin/env bash
#sets up the web servers for the deployment of web_static
apt-get update
apt-get -y install nginx
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
echo "<html>
  <head>
  </head>
  <body>
    Bismillah
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
sudo sed -i '51 i \\n\tlocation \/hbnb_static\/ {\n\t\talias \/data\/web_static\/current\/;\n\t}\n' /etc/nginx/sites-available/default
sudo service nginx restart
