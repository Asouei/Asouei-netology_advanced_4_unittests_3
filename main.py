import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time


def login_pass_enter(l, p):

    driver = webdriver.Chrome()
    driver.get('https://passport.yandex.ru/auth/')
    login = driver.find_element_by_id('passp-field-login')
    login.click()
    login.send_keys(l)
    login.send_keys(Keys.ENTER)
    time.sleep(1)
    try:
        password = driver.find_element_by_id('passp-field-passwd')
    except NoSuchElementException:
        return False
    password.send_keys(p)
    password.send_keys(Keys.ENTER)
    time.sleep(3)
    try:
        driver.find_element_by_link_text("Управление аккаунтом")
    except NoSuchElementException:
        return False
    return True





