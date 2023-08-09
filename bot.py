import os
import sys
from time import sleep
from chrome_dev.chrome_dev import ChromDevWrapper
from dotenv import load_dotenv
from logs import logger

class Bot (ChromDevWrapper):
    
    def __init__ (self, login_user:str, login_pass:str, chrome_path:str):
        """ Staore login data and initialize ChromeDevWrapper

        Args:
            login_user (str): login user for previred page
            login_pass (str): login password for previred page	
            chrome_path (str): path to chrome executable
        """
        
        
        self.login_user = login_user
        self.login_pass = login_pass
        self.chrome_path = chrome_path
        self.logs_base = f"(bot - {self.login_user})"
        
        self.selectors = {
            "login": {
                'user': '[id="rutUsuario:inputRutCC"]',
                'pass': '[id="usuarioClave:inputPassSC"]',
                'submit': '[type="submit"]',     
                'logout_button': 'button.cerrar-sesion[type="submit"]',
            }            
        }
        
        # Start chrome
        logger.info (f"{self.logs_base} starting chrome...")
        super().__init__(self.chrome_path)
        
    def login (self):
        """ Login with user credentials """
        
        logger.info (f"{self.logs_base} login...")
        
        # Load page and try login
        self.set_page ("https://controlcontratistas.previred.com/wControlContratistas/pages/login/Login.jsf")
        
        self.send_data_js (self.selectors["login"]["user"], self.login_user)
        self.send_data_js (self.selectors["login"]["pass"], self.login_pass)
        self.click (self.selectors["login"]["submit"])
        
        # Validate login
        sleep (5)
        logout_button = self.get_text (self.selectors["login"]["logout_button"])
        if logout_button:
            logger.info (f"{self.logs_base} logged")
        else:
            logger.error (f"{self.logs_base} login failed")
            sys.exit ()

    def auto_run (self):
        """ Run bot automatically:
            login
            ...
        """
        
        self.login ()

if __name__ == '__main__':
    
    # Test bot with debug data
    load_dotenv ()
    DEBUG_USER = os.getenv ("DEBUG_USER")
    DEBUG_PASS = os.getenv ("DEBUG_PASS") 
    CHROME_FOLDER = os.getenv ("CHROME_PATH")
    bot = Bot(DEBUG_USER, DEBUG_PASS, CHROME_FOLDER)
    bot.login()