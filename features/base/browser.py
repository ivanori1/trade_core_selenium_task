from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Browser(object):
    driver = webdriver.Chrome()
    driver.implicitly_wait(30)
    driver.set_page_load_timeout(30)
    driver.maximize_window()

    def close(context):
        context.driver.close()

    def navigate(self, address):
        self.driver.get(address)

    def get_page_title(self):
        return self.driver.title

    def get_by_type(context, locator_type):
        if locator_type == "css":
            return By.CSS_SELECTOR
        elif locator_type == "xpath":
            return By.XPATH
        else:
            print("Unknown selector")

    def get_element(context, locator, locator_type="css"):
        element = None
        try:
            by_type = context.get_by_type(locator_type)
            element = context.driver.find_element(by_type, locator)
        except:
            print("element not found " + locator)
        return element

    def click_on_element(context, locator, locator_type="css"):
        try:
            element = context.get_element(locator, locator_type)
            element.click()
        except:
            print("click action on element" + locator + " not executed")

    def wait_for_element_to_be_clickable(self, locator, locator_type="css"):
        by_type = self.get_by_type(locator_type)
        wait = WebDriverWait(self.driver, 20)
        element = wait.until(EC.element_to_be_clickable((by_type, locator)))
        return element

    def is_visible_element(self, locator, locator_type="css"):
        element_visible = self.get_element(locator, locator_type).is_displayed()
        return element_visible
