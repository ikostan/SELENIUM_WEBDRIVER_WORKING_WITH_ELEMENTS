import unittest
from selenium import webdriver
from config import ie_web_driver_path, test_title, test_url


class MyTestCase(unittest.TestCase):

    def test_ie_driver_works(self):

        driver = webdriver.Ie(executable_path=ie_web_driver_path)
        driver.get(test_url)
        url = driver.current_url
        driver.close()
        self.assertEqual(test_url, url)

