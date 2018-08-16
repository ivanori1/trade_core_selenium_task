from selenium.webdriver.common.by import By
from features.base.browser import Browser


class CreateAccountElements(object):

    # Home Page Locators
    _next_button = By.ID, "button-step"


class CreateAccount(Browser):
    # Home Page Actions

    def navigate(self, address):
        self.driver.get(address)

    def get_page_title(self):
        return self.driver.title

    def click_element(self, *locator):
        self.driver.find_element(*locator).click()

