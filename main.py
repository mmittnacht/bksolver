from const import *

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from helpers import *


driver = webdriver.Chrome()

driver.get("https://burgerkingelmenyem.hu/")

iframe = driver.find_element(By.CSS_SELECTOR, "iframe")

driver.switch_to.frame(iframe)


inputElement = driver.find_element(By.CSS_SELECTOR, ".InputText")
inputElement.send_keys(CODE)

click_next(driver)

inputElement = driver.find_element(By.CSS_SELECTOR, ".QWatchTimer")
inputElement.click()
inputElement.send_keys(Keys.RETURN)

select_time(driver)

click_next(driver)

while True:
    try:
        decide_with_question(driver)
    except NoSuchElementException as ex:
        print(ex)

        continue
# print(inputElement)
# print(driver.title)
