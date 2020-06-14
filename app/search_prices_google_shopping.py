from selenium.webdriver import Chrome as browser
from selenium.webdriver.common.keys import Keys

#from model.product_model import ProductModel

class SearchPricesGoogleShopping():

    def __init__(self, objBrowser: browser):
        self.browser = objBrowser

    def search(self, product):
        self.browser.find_element_by_css_selector("input.gsfi").send_keys(product + Keys.ENTER)
        self.browser.find_element_by_css_selector("input.gsfi").clear()
        return self.getProductFieldsFound()
    
    def getProductFieldsFound(self):
        listElements = self.browser.find_elements_by_class_name("sh-dlr__list-result")
        listProductsFound = []
        for element in listElements:
            dictElement = {
                "description" : element.find_element_by_css_selector("h3.xsRiS").text,
                "site" : element.find_element_by_css_selector("a.hy2WroIfzrX__merchant-name").get_attribute("href"),
                "price" : element.find_element_by_css_selector("span.Nr22bf").text,
            }
            listProductsFound.append(dictElement)
        return listProductsFound

if __name__ == "__main__":
    pass
