sudo apt-get install python-pip
sudo pip install Django==1.5
sudo apt-get install mysql-server
sudo apt-get install libjpeg-dev libfreetype6 libfreetype6-dev zlib1g-dev python-dev
sudo pip install PIL
sudo apt-get install python-mysqldb
sudo pip install django-grappelli==2.5.0
sudo pip install django-filebrowser


mysql> create user 'dews'@'localhost' identified by '<password>';
mysql> create database DEWS;
mysql> grant all privileges on DEWS.* to dews@localhost;


WSGIScriptAlias / /home/dews/DEWS/wsgi.py
WSGIPythonPath /home/dews

<VirtualHost *:80>
        ServerAdmin webmaster@localhost

        DocumentRoot /var/www

      <Directory /home/dews/DEWS>
         <Files wsgi.py>
           Order deny,allow
           Allow from all
         </Files>
      </Directory>
