#!/usr/bin/env bash

cd build/lib/
python3 ../../setup.py install
cd ../..

mkdir --parents  /var/www/pythonApps/pineappleProject
mkdir /var/www/pythonApps/pineappleProject/logs/

cp exampleConfigs/pineappleProject.wsgi /var/www/pythonApps/pineappleProject/
cp exampleConfigs/pineappleProject.conf /etc/apache2/sites-available
cp -r build/lib/pypineapple /var/www/pythonApps/pineappleProject/
cp -r build/lib/pypineapple/* /var/www/pythonApps/pineappleProject/
chown -R www-data /var/www/pythonApps/pineappleProject

a2dissite 000-default
a2ensite pineappleProject
apt-get install libapache2-mod-wsgi-py3 -y
systemctl restart apache2