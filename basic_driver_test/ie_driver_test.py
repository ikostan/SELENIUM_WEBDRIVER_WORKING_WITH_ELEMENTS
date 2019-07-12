import unittest
from selenium import webdriver
from config import ie_web_driver_path, test_title, test_url


class MyTestCase(unittest.TestCase):

    def test_ie_driver_works(self):

        driver = webdriver.Ie(executable_path=ie_web_driver_path)

        driver.maximize_window()
        driver.implicitly_wait(30)

        driver.get(test_url)
        url = driver.current_url
        title = driver.title

        self.assertEqual(test_url, url)
        self.assertEqual(test_title, title)

        driver.close()
        driver.quit()

