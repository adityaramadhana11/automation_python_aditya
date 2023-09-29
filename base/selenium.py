from utils.logger import LogGen
from traceback import print_stack

log=LogGen.log()

class selenium_driver:
    def click(driver, locator, logging=0):
        try:
            by_type, value = locator
            driver.find_element(by_type, value).click()
            if logging==1:
                log.info(f"clicked on element {locator}")
        except:
            log.error(f"cant click on element {locator}")
            print_stack()

    def sendkeys(driver, locator, data, logging=0):
        try:
            by_type, value = locator
            driver.find_element(by_type, value).send_keys(data)
            if logging==1:
                log.info(f"send data on element with locator {locator}")
        except:
            log.error(f"cannot send data on element with locator {locator}")
            print_stack()
    
    def gettext(driver, locator, logging=0):
        try:
            by_type, value = locator
            text = driver.find_element(by_type, value).text
            if logging==1:
                log.info(f"get text on element with locator {locator}")
        except:
            log.error(f"cannot get text on element with locator {locator}")
            print_stack()
        return text