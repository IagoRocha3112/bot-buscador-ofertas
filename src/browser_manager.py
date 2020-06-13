import os
from datetime import datetime
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv, find_dotenv

CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))
ENV_PATH = CURRENT_PATH + '/../.env'
load_dotenv(dotenv_path=ENV_PATH)


class BrowserManager():

    def __init__(self):
        """ 
        Author: Iago Rocha \n
        Class constructor
        - Param 0: void 
        """
        # Get properties of screen automatically
        dictPropScreen = self.getScreenSize()

        # Create instance Webdriver Chrome
        self.webdriver = self.createWebdriverChrome(
            dictPropScreen['width'], dictPropScreen['heigth'])


    def createWebdriverChrome(self, widthWindow, heightWindow, posX=0, posY=0, headless=False):
        """ 
        Author: Iago Rocha \n
        Set options and create Webdrive Chrome
        - Param 0: int | widthWindow
        - Param 1: int | heightWindow
        - Param 2: int | posX
        - Param 3: int | posY
        - Param 3: bool | headless
        - Return: object | webDriver
        """
        chromeOptions = Options()
        if headless is True:
            chromeOptions.add_argument('--headless')
        chromeOptions.add_argument('--no-sandbox')
        chromeOptions.add_argument('--disable-dev-shm-usage')
        chromeOptions.add_argument('--disable-notifications')
        # Config path chrome driver
        pathChromeDriver = CURRENT_PATH + '/../drivers/chromedriver'
        # Create object Chrome WebDriver
        webDriver = webdriver.Chrome(
            executable_path=pathChromeDriver, chrome_options=chromeOptions)
        # Position and size of window
        webDriver.set_window_size(widthWindow, heightWindow)
        webDriver.set_window_position(posX, posY)
        return webDriver

    def openPage(self, url):
        """ 
        Author: Iago Rocha \n
        Loads a web page in the current browser session
        - Param 0: str | url
        """
        self.webdriver.get(url)

    def closeBrowser(self):
        """ 
        Author: Iago Rocha \n
        Close the current window
        """
        self.webdriver.close()

    def getScreenSize(self):
        """ 
        Author: Iago Rocha \n
        Get properties of screen
        - Param 0: void
        - Return: dict | propertiesScreen 
            (keys: width, height)
        """
        # Desenvolver rotina para obter tamanho da tela automaticamente (opcional)
        propertiesScreen = {
            'width': 1024,
            'heigth': 768
        }
        return propertiesScreen


if __name__ == "__main__":
    pass
