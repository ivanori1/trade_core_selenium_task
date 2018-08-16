import unittest
from selenium import webdriver


class SampleTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def tradecore_test(self):
        self.driver.get("https://demo-biq.dev.tradecore.io/#/")
        assert self.driver.title == "TradeCore - Step 1 | Registration"

    def tearDown(self):
        self.driver.quit()