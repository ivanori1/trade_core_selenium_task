import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class SampleTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def tradecore_test(self):
        self.driver.get("https://demo-biq.dev.tradecore.io/#/")
        assert self.driver.title == "TradeCore - Step 1 | Registration"
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "myDynamicElement")))
    def select_country(self):

        select_dropdown =Select(self.driver.find_element_by_css_selector("#form-addr_country"))
        select_dropdown.select_by_visible_text("Armenia")


    def tearDown(self):
        self.driver.quit()