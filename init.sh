sudo unlink /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default

sudo /etc/init.d/mysql start
mysql -uroot -e "create database ask;"
mysql -uroot -e "CREATE USER 'django@localhost' IDENTIFIED BY 'django';"
mysql -uroot -e "GRANT ALL PRIVILEGES ON ask.* TO 'django@localhost';"
mysql -uroot -e "FLUSH PRIVELEGES;"
python /home/box/web/ask/manage.py makemigrations
python /home/box/web/ask/manage.py migrate
python /home/box/web/ask/manage.py check
sudo /etc/init.d/nginx restart
sudo gunicorn -c /home/box/web/etc/hello.py ask.wsgi:application