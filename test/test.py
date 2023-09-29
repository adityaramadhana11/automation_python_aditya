
import sys
sys.path.append("../")
from utils import webdriverfactory 
from selenium.webdriver.common.by import By
from pages.page_login import page_login
from pages.page_home import page_home
import time

def test_t001_login():
    driver = webdriverfactory.browser_driver("chrome")
    driver.get("https://www.saucedemo.com/")
    page_login.login_success(driver, "standard_user","secret_sauce")
    driver.close

def test_t002_login_failed():
    driver = webdriverfactory.browser_driver("chrome")
    driver.get("https://www.saucedemo.com/")
    page_login.login_failed(driver, "standard_user","xx")
    driver.close

def test_t003_login_empty_username():
    driver = webdriverfactory.browser_driver("chrome")
    driver.get("https://www.saucedemo.com/")
    page_login.login_username_empty(driver, "","secret_sauce")
    driver.close

def test_t004_click_item():
    driver = webdriverfactory.browser_driver("chrome")
    driver.get("https://www.saucedemo.com/")
    page_login.login_success(driver, "standard_user","secret_sauce")
    page_home.click_item(driver, "2")
    driver.close


