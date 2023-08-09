import os
from threading import Thread
from flask import Flask
from dotenv import load_dotenv
from logs import logger
from bot import Bot

LOGS_BASE = f"(app)"

app = Flask(__name__)
load_dotenv ()


@app.post("/")
def home ():
    """ Start bot """
    
    logger.info (f"{LOGS_BASE} new request")
        
    # TODO: get login data from request
    
    # Start bot in a thread
    DEBUG_USER = os.getenv ("DEBUG_USER")
    DEBUG_PASS = os.getenv ("DEBUG_PASS") 
    CHROME_FOLDER = os.getenv ("CHROME_PATH")
    bot = Bot(DEBUG_USER, DEBUG_PASS, CHROME_FOLDER)
    
    Thread(target=bot.auto_run).start()
    
    # TODO: update bot status in database
    
    # Return response
    return {
        "status": "ok",
        "message": "bot started",
        "data": []
    }
    

if __name__ == "__main__":
    app.run(debug=True)