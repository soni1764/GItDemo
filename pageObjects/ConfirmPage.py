from selenium.webdriver.common.by import By


class ConfirmPage:

    confirmbtn = (By.ID, "country")
    checkbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    submit = (By.CSS_SELECTOR, "input[type='submit']")
    alert = (By.CSS_SELECTOR, "div[class*='alert-success']")
    country = (By.LINK_TEXT, "India")

    def __init__(self, driver):
        self.driver = driver

    def confirm(self):
        return  self.driver.find_element(*ConfirmPage.confirmbtn)

    def select_country(self):
        return self.driver.find_element(*ConfirmPage.country)

    def clickcheckbox(self):
        return self.driver.find_element(*ConfirmPage.checkbox)

    def clciksubmit(self):
        return self.driver.find_element(*ConfirmPage.submit)

    def getalert(self):
        return self.driver.find_element(*ConfirmPage.alert)

    def getscreenshot(self):
        # self.driver.get_screenshot_as_file("C:\\Users\\Prashansha\\PycharmProjects\\PythonselFramework\\Result\\screen.png")
        self.driver.get_screenshot_as_file("..\\Report\\screen.png")
