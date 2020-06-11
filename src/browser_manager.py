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
        pass

    def settingsChrome(self):
        chromeOptions = Options()
        # chromeOptions.add_argument('--headless')
        chromeOptions.add_argument('--no-sandbox')
        chromeOptions.add_argument('--disable-dev-shm-usage')
        chromeOptions.add_argument('--disable-notifications')
        # Config path chrome driver
        pathChromeDriver = CURRENT_PATH + '/../drivers/chromedriver'
        # Create object Chrome WebDriver
        webDriver = webdriver.Chrome(
            executable_path=pathChromeDriver, chrome_options=chromeOptions)
        # Get properties of screen automatically
        dictWindowProperties = self.getWindowSize()
        webDriver.set_window_size(
            dictWindowProperties['width'], dictWindowProperties['heigth'])
        webDriver.set_window_position(0, 0)
        return webDriver

    def openPage(self, strUrl):
        pass

    def close(self):
        pass

    def getWindowSize(self):
        # Desenvolver rotina para obter tamanho da tela automaticamente (opcional)
        propertiesWindow = {
            'width': 1920,
            'heigth': 1080
        }
        return propertiesWindow


if __name__ == "__main__":
    pass
