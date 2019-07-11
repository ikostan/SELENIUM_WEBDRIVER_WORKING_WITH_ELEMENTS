import unittest
from selenium import webdriver
from config import test_title, test_url
from selenium.webdriver.opera.options import Options


class MyTestCase(unittest.TestCase):

    def test_opera_driver_works(self):

        options = Options()
        options.binary_location = r'C:\\Users\\superadmin\\AppData\\Local\\' \
                                  r'Programs\\Opera\\60.0.3255.95\\opera.exe'
        opera_web_driver_path = r'C:\\Users\\superadmin\\Desktop\\Python\\selenium\\' \
                                r'SELENIUM_WEBDRIVER_WORKING_WITH_ELEMENTS\\webdriver\\' \
                                r'opera\\win_64\\2.45\\operadriver.exe'
        driver = webdriver.Opera(options=options, executable_path=opera_web_driver_path)
        driver.get(test_url)
        title = driver.title
        driver.close()
        self.assertEqual(test_title, title)

