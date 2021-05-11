import pytest

from utilities.BaseClass import BaseClass
from pageObjects.HomePage import HomePage

class TestOne(BaseClass):

    def test_e2e(self):

        log = self.getlogger()
        homepage = HomePage(self.driver)        # Home page

        shoppingpage = homepage.shop_option()  # Shopping page
        log.info("Getting all the cards title")
        cards = shoppingpage.getcardtitles()
        for card in cards:
            cardText = card.text
            # print(cardText)
            log.info(cardText)
            if cardText == "Blackberry":
                shoppingpage.getcardfooterbtn().click()

        checkoutpage = shoppingpage.checkoutbtn()             # Checkout Page

        confirmpage = checkoutpage.finalcheckout()            # Confirm Page
        log.info("Entering Country name")
        confirmpage.confirm().send_keys("ind")
        # time.sleep(6)
        self.valifylinkpresence("India")
        confirmpage.select_country().click()

        confirmpage.clickcheckbox().click()
        confirmpage.clciksubmit().click()
        alerText = confirmpage.getalert().text
        # print(alerText)
        log.info(alerText)
        confirmpage.getscreenshot()
        assert "Success" in alerText
        # self.driver.get_screenshot_as_file("screen.png")


print("Remove this line1")
print("Remove this line2")

