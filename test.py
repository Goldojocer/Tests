from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()

driver = webdriver.Chrome(
    executable_path="D:\\pythonProject1\\chrome\\chromedriver.exe",
    options=options
)

try:
    driver.get("https://www.google.com/")
    time.sleep(1)

    search_input = driver.find_element_by_name("q")
    search_input.clear()
    search_input.send_keys("Калькулятор")
    time.sleep(1)
    search_input.send_keys(Keys.ENTER)
    time.sleep(1)

    click_input = driver.find_element_by_xpath('.//span[@class = "qv3Wpe"]')
    click_input = driver.find_element_by_xpath('.//div[@jsname = "N10B9"]').click()
    time.sleep(0.2)
    click_input = driver.find_element_by_xpath('.//div[@jsname = "YovRWb"]').click()
    time.sleep(0.2)
    click_input = driver.find_element_by_xpath('.//div[@jsname = "lVjWed"]').click()
    time.sleep(0.2)
    click_input = driver.find_element_by_xpath('.//div[@jsname = "pPHzQc"]').click()
    time.sleep(0.2)
    click_input = driver.find_element_by_xpath('.//div[@jsname = "KN1kY"]').click()
    time.sleep(0.2)
    click_input = driver.find_element_by_xpath('.//div[@jsname = "XSr6wc"]').click()
    time.sleep(0.2)
    click_input = driver.find_element_by_xpath('.//div[@jsname = "N10B9"]').click()
    time.sleep(0.2)
    click_input = driver.find_element_by_xpath('.//div[@jsname = "Pt8tGc"]').click()
    time.sleep(5)


except Exception as ex:
    print(ex)

finally:
    driver.close()
    driver.quit()