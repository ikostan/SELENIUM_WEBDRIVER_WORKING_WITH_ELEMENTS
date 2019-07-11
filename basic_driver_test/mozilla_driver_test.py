import unittest
from selenium import webdriver
from config import mozilla_web_driver_path, test_title, test_url


class MyTestCase(unittest.TestCase):

    def test_mozilla_driver_works(self):

        driver = webdriver.Firefox(executable_path=mozilla_web_driver_path)
        driver.get(test_url)
        url = driver.current_url
        title = driver.title
        driver.close()
        self.assertEqual(test_url, url)
        self.assertEqual(test_title, title)

