import unittest
from selenium import webdriver
from config import chrome_web_driver_path, test_title, test_url


class MyTestCase(unittest.TestCase):

    def test_chrome_driver_works(self):

        driver = webdriver.Chrome(executable_path=chrome_web_driver_path)
        driver.get(test_url)
        title = driver.title
        driver.close()
        self.assertEqual(test_title, title)

