git config --global user.email "604_fork@mail.ru"                              
git config --global user.name "604_fork"
sudo unlink /etc/nginx/sites-enabled/default
sudo unlink /etc/nginx/sites-enabled/test.conf
sudo unlink /etc/gunicorn.d/hello.py 
sudo ln -s /home/box/web/etc/gunicornConfig.py /etc/gunicorn.d/hello.py
sudo ln -s /home/box/web/etc/stepic.nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
