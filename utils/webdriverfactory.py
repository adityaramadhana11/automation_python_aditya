from selenium import webdriver

def browser_driver(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        return driver