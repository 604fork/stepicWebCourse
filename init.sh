sudo unlink /etc/nginx/sites-enabled/default
sudo unlink /etc/nginx/sites-enabled/test.conf
sudo ln -s /home/box/web/etc/stepic.nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
