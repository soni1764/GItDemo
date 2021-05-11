import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import logging
import inspect
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("setup")
class BaseClass:

    def valifylinkpresence(self, Text):

        wait = WebDriverWait(self.driver, 7)
        wait.until(EC.presence_of_element_located((By.LINK_TEXT, Text)))


    def getlogger(self):

        loggername = inspect.stack()[1][3]
        logger = logging.getLogger(loggername)

        # filehandler = logging.FileHandler("C:\\Users\\Prashansha\\PycharmProjects\\PythonselFramework\\Result\\logfile.log")
        filehandler = logging.FileHandler("..\\Report\\logfile.log")
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        filehandler.setFormatter(formatter)

        logger.addHandler(filehandler)
        logger.setLevel(logging.INFO)
        return logger

    def select_option(self, locator, text):
        sel = Select(locator)
        sel.select_by_visible_text(text)
