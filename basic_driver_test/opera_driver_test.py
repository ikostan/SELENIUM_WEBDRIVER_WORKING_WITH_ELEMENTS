import unittest
from selenium import webdriver
from config import test_title, test_url, opera_web_driver_path, opera_binary_path
from selenium.webdriver.opera.options import Options


class MyTestCase(unittest.TestCase):

    def test_opera_driver_works(self):

        options = Options()
        options.binary_location = opera_binary_path
        driver = webdriver.Opera(options=options, executable_path=opera_web_driver_path)
        driver.get(test_url)
        url = driver.current_url
        title = driver.title
        driver.close()
        self.assertEqual(test_url, url)
        self.assertEqual(test_title, title)

