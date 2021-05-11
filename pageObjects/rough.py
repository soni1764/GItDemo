from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
# chrome_options.add_argument("headless")

driver = webdriver.Chrome(executable_path="C:/chromedriver.exe", options=chrome_options)

driver.get("https://rahulshettyacademy.com/angularpractice/shop")

cards = driver.find_elements_by_css_selector(".card-title a")
# i = -1
for card in cards:
    # i = i+1
    cardText = card.text
    print(cardText)
    if cardText == "Blackberry":
        driver.find_element_by_css_selector(".card-footer button").click()

driver.find_element_by_css_selector("a[class*='btn-primary']").click()
driver.find_element_by_css_selector(".btn-success").click()
