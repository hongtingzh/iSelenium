import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class ISelenium(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()

    def test_baidu(self):

        self.driver.get("https://www.baidu.com")
        self.driver.find_element(By.ID, "kw").send_keys("selenium")
