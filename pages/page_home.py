from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils import webdriverfactory
import time

def item(number) : return By.XPATH, f'//*[@id="inventory_container"]/div[@class="inventory_list"]/div[{number}]/div[1]'

class page_home:
    def click_item(driver, item_number):
        driver.find_element(*item(item_number)).click()

