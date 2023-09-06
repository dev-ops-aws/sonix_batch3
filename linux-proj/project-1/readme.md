Script Title : How To Install Linux, Apache, MySQL, PHP (LAMP) stack on Ubuntu 22.04 
---------------------------

#!/bin/bash : Bash shell script for Installation of LAMP stacks which is used to create, host, and maintain web content. It is a popular solution that powers many of the websites you commonly use today.

---------------------------


Description: 
----------------------------

This Bash script installs the Lamp stack which is a combination of operating system and open-source software stack. This LAMP setup includes the installation of Apache HTTP Server, MySQL and PHP on the top of Ubuntu.

----------------------------


Prerequisites
----------------------------

Operating System : Ubuntu 22.04

SECURITY FIRST: Log into the remote machine as root: $sudo su -

SECURITY SECOND: Add a firewall. To list all currently available UFW application profiles, you can run: #sudo ufw app list

To only allow traffic on port 80, use the Apache profile: sudo ufw allow in "Apache"

You can verify the change with: sudo ufw status

----------------------------


Script Details:
-----------------------------

update and upgrade the apt-get packages to their current versions in your system.

Install the Apache web server on the linux which is acting as the base layer in the LAMP stack.

Install MySQL. It is used for collecting and storing the data as RDBMS.

Install PHP and requirements. PHP an object oriented scripting language is used to display the data in MySQL.

Install PhpMyAdmin. It is a free and open source administration tool for MySQL and MariaDB. As a portable web application written primarily in PHP, it has become one of the most popular MySQL administration tools, especially for web hosting services.

chown command changes the ownership to user:group i.e. www-data:www-data in our case.

command a2enmod enables apache2 module and phpenmod enables php module.

restart the apache2 web service.


-----------------------------


After successfully executing the script
-----------------------------

Go to a browser and hit the following

1) http://your_server_ip - You’ll see the default Ubuntu 20.04 Apache web page, which is there for informational and testing purposes.
 
2) http://your_server_ip/phpmyadmin - For accessing phpmyadmin page.
 

 -----------------------------
