import unittest
from selenium import webdriver
from config import chrome_web_driver_path, test_title, test_url


class MyTestCase(unittest.TestCase):

    def test_chrome_driver_works(self):

        driver = webdriver.Chrome(executable_path=chrome_web_driver_path)

        driver.maximize_window()
        driver.get(test_url)
        url = driver.current_url
        title = driver.title

        self.assertEqual(test_url, url)
        self.assertEqual(test_title, title)

        driver.close()

