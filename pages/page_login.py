
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils import webdriverfactory
import time
from base.selenium import selenium_driver as sd
from utils.logger import LogGen

log=LogGen.log()

field_username = By.XPATH, "//input[@id='user-name']"
field_password = By.XPATH, "//input[@id='password']"
button_login = By.ID, "login-button"
header_homepage =  By.XPATH, "//div[contains(text(),'Swag Labs')]"
text_login_failed = By.XPATH, "//h3[contains(text(),'Username and password do not match any user in this service')]"
text_username_blank = By.XPATH, "//h3[contains(text(),'Epic sadface: Username is required')]"

class page_login:

    def login(driver,username,password):
        sd.sendkeys(driver, field_username, username)
        sd.sendkeys(driver, field_password, password)
        sd.click(driver, button_login)

    def login_success(driver, username, password):   
        page_login.login(driver, username, password)
        header_text = sd.gettext(driver, header_homepage)
        if header_text == 'Swag Labs':
            log.info("login success")
            assert True
        else:
            log.error("login failed")
            assert False

    def login_failed(driver, username, password):   
        page_login.login(driver, username, password)
        text_failed = sd.gettext(driver, text_login_failed)
        if text_failed == 'Epic sadface: Username and password do not match any user in this service':
            log.info(f"text match\nexpected: Epic sadface: Username and password do not match any user in this service\nactual: {text_failed}")
            assert True
        else:
            log.error(f"text not match\nexpected: Epic sadface: Username and password do not match any user in this service\nactual: {text_failed}")
            assert False

    def login_username_empty(driver, username, password):   
        page_login.login(driver, username, password)
        text_failed =sd.gettext(driver, text_username_blank)
        if text_failed == 'Epic sadface: Username is required':
            log.info(f"text match\nexpected: Epic sadface: Username is required\nactual: {text_failed}")
            assert True
        else:
            log.error(f"text not match\nexpected: Epic sadface: Username is required\nactual: {text_failed}")
            assert False
    