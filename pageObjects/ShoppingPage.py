from selenium.webdriver.common.by import By
from pageObjects.CheoutPage import CheckoutPage

class ShoppingPage:
    card_title = (By.CSS_SELECTOR, ".card-title a")
    card_footer = (By.CSS_SELECTOR, ".card-footer button")
    primarybtn = (By.CSS_SELECTOR, "a[class*='btn-primary']")

    def __init__(self, driver):
        self.driver = driver

    def getcardtitles(self):
        return self.driver.find_elements(*ShoppingPage.card_title)

    def getcardfooterbtn(self):
        return self.driver.find_element(*ShoppingPage.card_footer)

    def checkoutbtn(self):
        self.driver.find_element(*ShoppingPage.primarybtn).click()
        checkoutpage = CheckoutPage(self.driver)
        return checkoutpage
