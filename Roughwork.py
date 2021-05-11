from selenium import webdriver
# import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
# chrome_options.add_argument("headless")

driver = webdriver.Chrome(executable_path="C:/chromedriver.exe", options=chrome_options)

driver.get("https://rahulshettyacademy.com/angularpractice")

# driver.find_elements_by_css_selector("a[href*='/angularpractice/shop']").click()
driver.find_element_by_xpath("//a[text()='Shop']").click()
products = driver.find_elements_by_xpath("//div[@class='card h-100']")

for product in products:
    print(product.find_element_by_xpath("div/h4/a").text)
    productname = product.find_element_by_xpath("div/h4/a").text
    if productname == "Blackberry":
        product.find_element_by_xpath("div/button").click()

driver.find_element_by_css_selector("a[class*='btn-primary']").click()
driver.find_element_by_css_selector("button[class*='btn-success']").click()

driver.find_element_by_id("country").send_keys("ind")
# time.sleep(6)
wait = WebDriverWait(driver, 7)
wait.until(EC.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element_by_link_text("India").click()

driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
driver.find_element_by_css_selector("input[type='submit']").click()
print(driver.find_element_by_class_name("alert-success").text)
assert "Success" in driver.find_element_by_css_selector(".alert-success").text
driver.get_screenshot_as_file("screen.png")
