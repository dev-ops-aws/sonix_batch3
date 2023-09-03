How To Install Linux, Apache, MySQL, PHP (LAMP) stack on Ubuntu 22.04
Deliver high-performance web apps and websites with the LAMP stack. LAMP is a bundle of open source software that you can use to create a solid and reliable foundation for your web app development. The following components are included in the LAMP stack:

Linux as the operating system
Apache HTTP Server as the webserver
MySQL as the database
PHP as the programming language


SECURITY FIRST: 
Log into the remote machine as root: sudo su -

SECURITY SECOND: Add a firewall.
To list all currently available UFW application profiles, you can run:


#sudo ufw app list
To only allow traffic on port 80, use the Apache profile:

# sudo ufw allow in "Apache"
You can verify the change with:
# sudo ufw status

LAMP installation and setup
Install Apache
# su sudo apt update
# su apt install apache2 -y

Install MySQL
# sudo apt install mysql-server mysql-client -y
Run the MySQL secure installation
# sudo mysql_secure_installation
This will ask if you want to configure the VALIDATE PASSWORD PLUGIN.
Answer Y for yes, or anything else to continue without enabling.


1. Database creation
Log into MySQL
# sudo mysql 

Create a new database
# CREATE DATABASE mydb;

User creation
Add your user to MySQL

# CREATE USER username@localhost IDENTIFIED VIA mysql_native_password BY ‘password’;

# UPDATE user SET password=PASSWORD('password') WHERE User='username' AND Host = 'localhost';

3. Grant all privileges to the user on a specific database. Only allow access from localhost (this is the most secure and common configuration you will use for a web application). This will probably be the new sudo user you have set up previously.
# GRANT ALL ON mydb.* TO 'username'@'laocalhost';

4. Now exit the MySQL shell with:

# exit


Install PHP
# apt-get install php libapache2-mod-php php-mysql -y
Enabling Modules
# sudo a2enmod rewrite
# sudo phpenmod mcrypt

Additionally you will need
# sudo chown -R www-data:www-data /var/www

Configure PhpMyAdmin
# echo 'Include /etc/phpmyadmin/apache.conf' >> /e>

Restarting Apache
# sudo service apache2 restart
# echo -e "\n\nLAMP Installation Completed"
exit 0
