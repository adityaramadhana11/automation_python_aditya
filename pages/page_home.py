from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils import webdriverfactory
import time
from utils.logger import LogGen
from base.selenium import selenium_driver as sd

log=LogGen.log()

def item(number) : return By.XPATH, f'//*[@id="inventory_container"]/div[@class="inventory_list"]/div[{number}]/div[1]'

class page_home:
    def click_item(driver, item_number):
        sd.click(driver, item(item_number))

