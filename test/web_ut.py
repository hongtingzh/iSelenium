import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class ISelenium(unittest.TestCase):

    def tearDown(self) -> None:
        self.driver.quit()

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path='../drivers/chromedriver.exe')
        sleep(3)

    def test_webui_1(self):
        self._test_baidu("今日头条", "test_webui_1")

    def test_webui_2(self):
        self._test_baidu("王者荣耀", "test_webui_2")

    def _test_baidu(self, search_keyword, testcase_name):
        self.driver.get('https://www.baidu.com')
        sleep(2)

        elem = self.driver.find_element(By.ID, "kw")
        elem.send_keys(f'{search_keyword}{Keys.RETURN}')
        sleep(3)



