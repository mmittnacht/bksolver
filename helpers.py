from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

from const import *
import time

def click_next(driver: WebDriver):
    btn = driver.find_element(By.ID, "NextButton")
    # this is needed because it's not a fucking button but an input type="button"
    driver.execute_script("arguments[0].click();", btn)

    time.sleep(1)


def select_time(driver: WebDriver):
    time_selectors = driver.find_elements(By.CSS_SELECTOR, ".MatrixDL.QWatchTimer")

    hour_selector = Select(time_selectors[0])
    sec_selector = Select(time_selectors[1])
    daytime_selector = Select(time_selectors[2])

    hour_selector.select_by_value(HOUR)
    sec_selector.select_by_value(SEC)
    daytime_selector.select_by_value(DAYTIME)


def select_normal_answer(driver: WebDriver):
    # select with .Selection
    try:
        elem = check_if_no_present(driver)
        if elem != False:
             elem.click()
        else:
            elem = driver.find_element(By.CSS_SELECTOR, ".Selection")

            elem.click()

        time.sleep(0.5)

        click_next(driver)
    except NoSuchElementException as ex:
        select_normal_answer(driver)


def select_label_answer(driver: WebDriver):
    # select with .LabelContainer
    try:
        elem = driver.find_element(By.CSS_SELECTOR, ".LabelContainer")

        elem.click()

        time.sleep(0.5)

        click_next(driver)
    except NoSuchElementException as ex:
        select_label_answer(driver)

    except Exception as ex:
        print(ex)


def select_question_answer(driver: WebDriver):
    # select with .QuestionBody
    try:
        click_next(driver)
    except NoSuchElementException as ex:
        select_question_answer(driver)


def select_bullet_answer(driver: WebDriver):
    # select with td.c4
    elems = driver.find_elements(By.CSS_SELECTOR, "td.c4")

    for elem in elems:
        elem.click()

    time.sleep(0.5)

    click_next(driver)


def check_if_no_present(driver: WebDriver):
    elems = driver.find_elements(By.CSS_SELECTOR, ".QuestionBody .ChoiceStructure .Selection .SingleAnswer")

    for elem in elems:
        if elem.get_attribute("textContent") == 'Nem':
            return elem
        
    return False


def get_bullet_body(driver: WebDriver):
    return len(driver.find_elements(By.CSS_SELECTOR, ".q-matrix")) > 0


def get_label_body(driver: WebDriver):
    return len(driver.find_elements(By.CSS_SELECTOR, ".LabelContainer")) > 0


def get_normal_body(driver: WebDriver):
    return len(driver.find_elements(By.CSS_SELECTOR, ".QuestionBody .ChoiceStructure .Selection")) > 0


def get_select_question_body(driver: WebDriver):
    return len(driver.find_elements(By.CSS_SELECTOR, ".QuestionBody .ChoiceStructure")) > 0


def decide_with_question(driver: WebDriver):
    time.sleep(1)

    if get_bullet_body(driver):
        print("Bullet")
        select_bullet_answer(driver)

        return

    if get_label_body(driver):
        print("Label")
        select_label_answer(driver)

        return
    
    if get_normal_body(driver):
        print("Normal")
        select_normal_answer(driver)

        return
    
    if get_select_question_body(driver):
        print("Question")
        select_question_answer(driver)

        return


