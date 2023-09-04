   Link  https://tecadmin.net/install-sendmail-on-ubuntu/

   
 How to Install and Configure Sendmail on Ubuntu 22.04 / 20.04 /18.04

Sendmail is a widely used Mail Transfer Agent (MTA) that allows users to send and receive email on Linux systems. It is a powerful and flexible mail server solution that can be configured to work with various email clients and services.

1. Update your system

     $ 𝐬𝐮𝐝𝐨 𝐚𝐩𝐭 𝐮𝐩𝐝𝐚𝐭𝐞 && 𝐬𝐮𝐝𝐨 𝐚𝐩𝐭 𝐮𝐩𝐠𝐫𝐚𝐝𝐞 -𝐲

 
2. Install Sendmail and related packages

   To install Sendmail along with related packages, such as 𝐦𝐚𝐢𝐥𝐮𝐭𝐢𝐥𝐬 and 𝐬𝐞𝐧𝐝𝐦𝐚𝐢𝐥-𝐜𝐟, run the following command

    $ 𝐬𝐮𝐝𝐨 𝐚𝐩𝐭 𝐢𝐧𝐬𝐭𝐚𝐥𝐥 -𝐲 𝐬𝐞𝐧𝐝𝐦𝐚𝐢𝐥 𝐬𝐞𝐧𝐝𝐦𝐚𝐢𝐥-𝐜𝐟 𝐦𝐚𝐢𝐥𝐮𝐭𝐢𝐥𝐬


  3. Configure Sendmail

       The main configuration file for 𝐒𝐞𝐧𝐝𝐦𝐚𝐢𝐥 𝐢𝐬 /𝐞𝐭𝐜/𝐦𝐚𝐢𝐥/𝐬𝐞𝐧𝐝𝐦𝐚𝐢𝐥.𝐜𝐟

       To configure Sendmail, open the /etc/mail/sendmail.mc file using your preferred text editor:

          $ 𝐬𝐮𝐝𝐨 𝐧𝐚𝐧𝐨 /𝐞𝐭𝐜/𝐦𝐚𝐢𝐥/𝐬𝐞𝐧𝐝𝐦𝐚𝐢𝐥.𝐦𝐜

               #!/bin/bash  𝐝𝐞𝐟𝐢𝐧𝐞(`𝐒𝐌𝐀𝐑𝐓_𝐇𝐎𝐒𝐓', `𝐲𝐨𝐮𝐫.𝐬𝐦𝐭𝐩.𝐬𝐞𝐫𝐯𝐞𝐫')𝐝𝐧𝐥

               𝐝𝐞𝐟𝐢𝐧𝐞(`𝐜𝐨𝐧𝐟𝐀𝐔𝐓𝐇_𝐌𝐄𝐂𝐇𝐀𝐍𝐈𝐒𝐌𝐒', `𝐄𝐗𝐓𝐄𝐑𝐍𝐀𝐋 𝐆𝐒𝐒𝐀𝐏𝐈 𝐃𝐈𝐆𝐄𝐒𝐓-𝐌𝐃𝟓 𝐂𝐑𝐀𝐌-𝐌𝐃𝟓 𝐋𝐎𝐆𝐈𝐍 𝐏𝐋𝐀𝐈𝐍')𝐝𝐧𝐥

             𝐅𝐄𝐀𝐓𝐔𝐑𝐄(`𝐚𝐮𝐭𝐡𝐢𝐧𝐟𝐨',`𝐡𝐚𝐬𝐡 -𝐨 /𝐞𝐭𝐜/𝐦𝐚𝐢𝐥/𝐚𝐮𝐭𝐡𝐢𝐧𝐟𝐨.𝐝𝐛')𝐝𝐧𝐥

         Replace 𝐲𝐨𝐮𝐫.𝐬𝐦𝐭𝐩.𝐬𝐞𝐫𝐯𝐞𝐫 with the address of your SMTP relay or smart host

4:  Set up authentication

   create the /𝐞𝐭𝐜/𝐦𝐚𝐢𝐥/𝐚𝐮𝐭𝐡𝐢𝐧𝐟𝐨 file

       $  𝐬𝐮𝐝𝐨  𝐧𝐚𝐧𝐨 /𝐞𝐭𝐜/𝐦𝐚𝐢𝐥/𝐚𝐮𝐭𝐡𝐢𝐧𝐟𝐨

     #!/bin/bash 𝐀𝐮𝐭𝐡𝐈𝐧𝐟𝐨:𝐲𝐨𝐮𝐫.𝐬𝐦𝐭𝐩.𝐬𝐞𝐫𝐯𝐞𝐫 "𝐔:𝐲𝐨𝐮𝐫_𝐮𝐬𝐞𝐫𝐧𝐚𝐦𝐞" "𝐏:𝐲𝐨𝐮𝐫_𝐩𝐚𝐬𝐬𝐰𝐨𝐫𝐝"

  Replace 𝐲𝐨𝐮𝐫.𝐬𝐦𝐭𝐩.𝐬𝐞𝐫𝐯𝐞𝐫, 𝐲𝐨𝐮𝐫_𝐮𝐬𝐞𝐫𝐧𝐚𝐦𝐞, and 𝐲𝐨𝐮𝐫_𝐩𝐚𝐬𝐬𝐰𝐨𝐫𝐝 with the appropriate values for your SMTP server.

     To create the authentication database, run

             $ 𝐬𝐮𝐝𝐨 𝐦𝐚𝐤𝐞𝐦𝐚𝐩 𝐡𝐚𝐬𝐡 /𝐞𝐭𝐜/𝐦𝐚𝐢𝐥/𝐚𝐮𝐭𝐡𝐢𝐧𝐟𝐨 < /𝐞𝐭𝐜/𝐦𝐚𝐢𝐥/𝐚𝐮𝐭𝐡𝐢𝐧𝐟𝐨

5:  Generate the Sendmail configuration file

   After making changes to the /𝐞𝐭𝐜/𝐦𝐚𝐢𝐥/𝐬𝐞𝐧𝐝𝐦𝐚𝐢𝐥.𝐦𝐜  file, you need to generate the /𝐞𝐭𝐜/𝐦𝐚𝐢𝐥/𝐬𝐞𝐧𝐝𝐦𝐚𝐢𝐥.𝐜𝐟 file. Run the following command

    $ 𝐬𝐮𝐝𝐨 𝐦𝐚𝐤𝐞 -𝐂 /𝐞𝐭𝐜/𝐦𝐚𝐢𝐥

6:  Start and enable the Sendmail service

    $ 𝐬𝐮𝐝𝐨 𝐬𝐲𝐬𝐭𝐞𝐦𝐜𝐭𝐥 𝐞𝐧𝐚𝐛𝐥𝐞 𝐬𝐞𝐧𝐝𝐦𝐚𝐢𝐥.𝐬𝐞𝐫𝐯𝐢𝐜𝐞


To ensure that Sendmail is running without errors, you can check its status

      $ 𝐬𝐮𝐝𝐨 𝐬𝐲𝐬𝐭𝐞𝐦𝐜𝐭𝐥 𝐬𝐭𝐚𝐭𝐮𝐬 𝐬𝐞𝐧𝐝𝐦𝐚𝐢𝐥𝐈𝐧𝐛𝐨𝐱

7: Test your Sendmail configuration

    $ echo "This is a test email." | mail -s "Test Email" recipient@example.com 

    

    

           






    

    
     

 


     

              




