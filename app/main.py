from time import sleep
from browser_manager import BrowserManager
from search_prices_google_shopping import SearchPricesGoogleShopping

class Main():

    def __init__(self):
        # initialization all objects
        self.browserManager = BrowserManager()
        self.browserManager.openPage('https://www.google.com.br/shopping')
        self.searchGoogle = SearchPricesGoogleShopping(self.browserManager.webdriver)

    def testing(self):
        products = [
            'Iphone',
            'Smartphone Xiaomi',
            'Smartphone Samsung',
            'Smartphone Asus'
        ]
        for product in products:
            print(self.searchGoogle.search(product), "\n")
            sleep(1)

if __name__ == "__main__":
    main = Main()
    # Testing
    main.testing()
    # Close browser
    main.browserManager.closeBrowser()
