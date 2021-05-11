from selenium.webdriver.common.by import By
from pageObjects.ConfirmPage import ConfirmPage

class CheckoutPage:
    confirmbtn = (By.CSS_SELECTOR, "button[class*='btn-success']")

    def __init__(self, driver):
        self.driver = driver

    def finalcheckout(self):
        # return self.driver.find_element(*CheckoutPage.confirmbtn)
        self.driver.find_element(*CheckoutPage.confirmbtn).click()
        confirmpage = ConfirmPage(self.driver)
        return confirmpage




