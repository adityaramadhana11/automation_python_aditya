
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils import webdriverfactory
import time


field_username = By.XPATH, "//input[@id='user-name']"
field_password = By.XPATH, "//input[@id='password']"
button_login = By.ID, "login-button"
header_homepage =  By.XPATH, "//div[contains(text(),'Swag Labs')]"
text_login_failed = By.XPATH, "//h3[contains(text(),'Username and password do not match any user in this service')]"
text_username_blank = By.XPATH, "//h3[contains(text(),'Epic sadface: Username is required')]"

class page_login:

    def login(driver,username,password):
        driver.find_element(*field_username).send_keys(username)
        driver.find_element(*field_password).send_keys(password)
        driver.find_element(*button_login).click()

    def login_success(driver, username, password):   
        page_login.login(driver, username, password)
        header_text = driver.find_element(*header_homepage).text
        if header_text == 'Swag Labs':
            print("login success")
            assert True
        else:
            print("login failed")
            assert False

    def login_failed(driver, username, password):   
        page_login.login(driver, username, password)
        text_failed = driver.find_element(*text_login_failed).text
        if text_failed == 'Epic sadface: Username and password do not match any user in this service':
            print("text match")
            assert True
        else:
            print("text not match")
            assert False

    def login_username_empty(driver, username, password):   
        page_login.login(driver, username, password)
        text_failed = driver.find_element(*text_username_blank).text
        if text_failed == 'Epic sadface: Username is required':
            print("text match")
            assert True
        else:
            print("text not match")
            assert False
    