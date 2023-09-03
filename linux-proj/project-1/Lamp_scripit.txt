#!/bin/bash
#Bash script to install an LAMP stack in ubuntu
#Updating Apt Packages and upgrading latest patches
sudo apt update -y && sudo apt upgrade -y
#Installing Apache2 Web server
sudo apt install apache2 apache2-doc apache2-utils libexpat1 ssl-cert -y
#Installing PHP 
sudo apt install php libapache2-mod-php php-mysql -y
#Install MySQL database server
sudo apt install mysql-server mysql-client -y
#Permissions for /var/www
sudo chown -R www-data:www-data /var/www
#Enabling Modules
sudo a2enmod rewrite
sudo phpenmod mcrypt
#Install PhpMyAdmin
sudo apt install phpmyadmin -y
#Configure PhpMyAdmin
echo 'Include /etc/phpmyadmin/apache.conf' >> /etc/apache2/apache2.conf
#Restarting Apache
sudo service apache2 restart
echo -e "\n\nLAMP Installation Completed"
exit 0

