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
new_str="listen \[\:\:\]\:80 default_server\n\n\tlocation \/hbnb_static {\n\t\talias \/data\/web_static\/current\/\n\t};"
sudo sed -i "s/listen \[\:\:\]\:80 default_server;/$new_str/" /etc/nginx/sites-available/default
sudo service nginx restart
