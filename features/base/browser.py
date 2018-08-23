from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class Browser(object):
    driver = webdriver.Chrome()
    driver.implicitly_wait(30)
    driver.set_page_load_timeout(30)
    driver.maximize_window()

    def close(context):
        context.driver.close()

    def navigate(self, address):
        self.driver.get(address)

    def get_page_url(self):
        return self.driver.current_url

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

    def send_keys_to_element(self, data, locator, locator_type="css"):
        try:
            element = self.get_element(locator, locator_type)
            element.clear()
            element.send_keys(data)
        except:
            print("send keys not performed on: " + locator)

    def wait_for_element_to_be_visible(self, locator, locator_type="css"):
        by_type = self.get_by_type(locator_type)
        wait = WebDriverWait(self.driver, 30)
        element = wait.until(EC.presence_of_element_located((by_type, locator)))
        return element

    def wait_for_element_to_be_clickable(self, locator, locator_type="css"):
        by_type = self.get_by_type(locator_type)
        wait = WebDriverWait(self.driver, 20)
        element = wait.until(EC.element_to_be_clickable((by_type, locator)))
        return element

    def wait_for_title(self, title):
        wait = WebDriverWait(self.driver, 20)
        element = wait.until(EC.title_is(title))
        return element

    def is_visible_element(self, locator, locator_type="css"):
        element_visible = self.get_element(locator, locator_type).is_displayed()
        return element_visible

    def select_from_dropdown(self, visible_text, locator, locator_type="css"):
        try:
            select_dropdown = Select(self.get_element(locator, locator_type))
            select_dropdown.select_by_visible_text(visible_text)
            print("Selected element is: " + visible_text)

        except:

            print("element not found " + locator)

    def text_of_element(self, inner_text, locator, locator_type="css"):
        element_text = self.get_element(locator, locator_type).text
        if element_text == inner_text:
            return True
        else:
            print("Compared text " + element_text + " and " + inner_text + " do not match")
            return False

    def attribute_value_of_element(self, attribute_name, locator, locator_type="css"):
        try:
            element = self.get_element(locator, locator_type)
            element_attribute = element.get_attribute(attribute_name)
            print("Value of attribute " + attribute_name + " from locator" + locator)
            return element_attribute
        except:
            print("Attribute " + attribute_name + " or element with locator " + locator + "not found")

    def is_selected_element(self, locator, locator_type="xpath"):
        element_is_selected = self.get_element(locator, locator_type).is_selected()
        return element_is_selected
