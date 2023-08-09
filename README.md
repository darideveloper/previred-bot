<div><a href='https://github.com/darideveloper/previred-bot/blob/master/LICENSE' target='_blank'>
                <img src='https://img.shields.io/github/license/darideveloper/previred-bot.svg?style=for-the-badge' alt='MIT License' height='30px'/>
            </a><a href='https://www.linkedin.com/in/francisco-dari-hernandez-6456b6181/' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=LinkedIn&color=0A66C2&logo=LinkedIn&logoColor=FFFFFF&label=' alt='Linkedin' height='30px'/>
            </a><a href='https://t.me/darideveloper' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=Telegram&color=26A5E4&logo=Telegram&logoColor=FFFFFF&label=' alt='Telegram' height='30px'/>
            </a><a href='https://github.com/darideveloper' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=GitHub&color=181717&logo=GitHub&logoColor=FFFFFF&label=' alt='Github' height='30px'/>
            </a><a href='https://www.fiverr.com/darideveloper' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=Fiverr&color=222222&logo=Fiverr&logoColor=1DBF73&label=' alt='Fiverr' height='30px'/>
            </a><a href='https://discord.com/users/992019836811083826' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=Discord&color=5865F2&logo=Discord&logoColor=FFFFFF&label=' alt='Discord' height='30px'/>
            </a><a href='mailto:darideveloper@gmail.com?subject=Hello Dari Developer' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=Gmail&color=EA4335&logo=Gmail&logoColor=FFFFFF&label=' alt='Gmail' height='30px'/>
            </a><a href='https://www.twitch.tv/darideveloper' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=Twitch&color=b9a3e3&logo=Twitch&logoColor=ffffff&label=' alt='Twitch' height='30px'/>
            </a></div><div align='center'><br><br><img src='https://github.com/darideveloper/previred-bot/blob/master/logo.png?raw=true' alt='Previred Bot' height='80px'/>



# Previred Bot

Bot for download files from [controlcontratistas.previred.com/wControlContratistas/](https://controlcontratistas.previred.com/wControlContratistas/), and place them in specific folder. 

The project starts using a Flask API.

Project type: **client**

</div><br><details>
            <summary>Table of Contents</summary>
            <ol>
<li><a href='#buildwith'>Build With</a></li>
<li><a href='#media'>Media</a></li>
<li><a href='#install'>Install</a></li>
<li><a href='#settings'>Settings</a></li>
<li><a href='#run'>Run</a></li>
<li><a href='#deploy'>Deploy</a></li>
<li><a href='#roadmap'>Roadmap</a></li></ol>
        </details><br>

# Build with

<div align='center'><a href='https://github.com/marty90/PyChromeDevTools' target='_blank'> <img src='https://cdn.svgporn.com/logos/chrome.svg' alt='PyChromeDevTools' title='PyChromeDevTools' height='50px'/> </a><a href='https://flask.palletsprojects.com/en/2.2.x/' target='_blank'> <img src='https://cdn.svgporn.com/logos/flask.svg' alt='Flask' title='Flask' height='50px'/> </a></div>

# Media

![logged](https://github.com/darideveloper/previred-bot/blob/master/screenshots/logged.png?raw=true)

![login](https://github.com/darideveloper/previred-bot/blob/master/screenshots/login.png?raw=true)

![terminal](https://github.com/darideveloper/previred-bot/blob/master/screenshots/terminal.png?raw=true)

# Install

## Third party modules

Install all modules from pip: 

``` bash
$ pip install -r requirements.txt
```

## Programs

To run the project, the following software must be installed:

* Python >= 3.10

# Settings

## Enviroment variables

In the file *.env*, are the main options and settings of the project.

Create a **.env** file, and place the following content

```bash
CHROME_PATH = C:Program FilesGoogleChromeApplicationchrome.exe
DEBUG_USER = {page user}
DEBUG_PASS = {page pass}
```

*Note: you can see as reference the **sample.env** file*

### CHROME_PATH

Path or  `chrome` executable path, in your system (in windows nu default *C:Program FilesGoogleChromeApplicationchrome.exe* )

### DEBUG_USER

User name to login during development (in future versions, the project will get the login credentials from api request)

### DEBUG_PASS

User password to login during development (in future versions, the project will get the login credentials from api request)

# Run

## Run API

For run the flask app (in local), just run with your python interpreter the file `app.py`: 

```bash
$ python app.py
```

## Start bot

To run the bot, just send an empty post request to the app. 
You can use this [postman workspace](https://www.postman.com/daridev/workspace/previred-bot/overview), just be sure to change (is is required) the variable `api_base` in the `api` collection.

# Deploy

Because this project need run a Google Chrome instance, for run it, you need a Virtual Machine (VM) or a Virtual Private Service (VPS)

# Roadmap

* [X] Start with api
* [ ] Get login data from api
* [X] Start bot
* [X] Login
* [ ] Only open one bot at time
* [ ] Download files
* [ ] Place downloaded files in specific folders

