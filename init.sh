sudo unlink /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo gunicorn -c /home/box/web/etc/hello.py ask.wsgi:application
sudo /etc/init/d/mysql start
sudo mysql -uroot -e "create database ask"