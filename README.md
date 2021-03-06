# scraping-instagram
This repository indicates how you can extract a user's instagram posts

# - Windows 

--> Install `chromedriver.exe`:

    [1] ayuda/información de Google Chrome
    
![](https://i.imgur.com/xnYl8UR.png) 
    
    [2] Check your version of Google Chrome
    
![](https://i.imgur.com/5YUxc6S.png)

    [3] Download the correct version: https://chromedriver.chromium.org/downloads

![](https://i.imgur.com/x6YSuW2.png)
![](https://i.imgur.com/A0XkTE4.png)

    [4] Then move the .zip to the project folder

![](https://i.imgur.com/1AT4upX.png)

    [5] Extract the .zip file to the project folder

![](https://i.imgur.com/94Mdntj.png)

    [6] In case of using linux you should modify the system.json file

![](https://i.imgur.com/j56UE70.png)

    [*] You will have to run the following commands
   
        >> Parrot OS
        [1] $ sudo apt install nodejs
        [2] $ sudo apt install npm
        [3] $ sudo npm -g install chromedriver
        [4] $ sudo ln -sf /usr/local/lib/node_modules/chromedriver/lib/chromedriver/chromedriver /usr/bin/chromedriver
        
        >> Ubuntu
        [1] $ sudo apt install nodejs
        [2] $ sudo apt install npm
        [3] $ sudo npm -g install chromedriver
        [4] $ sudo ln -sf /usr/lib/node_modules/chromedriver/lib/chromedriver/chromedriver ~/bin/chromedriver

# Check that you have all the necessary files
![](https://i.imgur.com/ViszOV0.png)

# Enter your username and password in the instagram_credentials.json

    >> For instance:
    
![](https://i.imgur.com/iX25HLb.png)
