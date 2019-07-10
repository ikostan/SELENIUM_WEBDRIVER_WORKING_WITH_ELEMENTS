import unittest
from selenium import webdriver
from config import ie_web_driver_path, test_title, test_url


class MyTestCase(unittest.TestCase):

    def test_edge_driver_works(self):

        driver = webdriver.Ie(ie_web_driver_path)
        driver.get(test_url)
        driver.implicitly_Wait(10)
        title = driver.title
        driver.quit()
        self.assertEqual(test_title, title)

