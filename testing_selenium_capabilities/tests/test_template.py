import unittest
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from drivers.driver import Driver


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = None

    def setUp(self):
        self.driver = None

    def test_chrome(self):
        browser = 'chrome'
        self.generic_method(browser)
        pass

    def test_ie(self):
        browser = 'ie'
        self.generic_method(browser)
        pass

    def test_opera(self):
        browser = 'opera'
        self.generic_method(browser)
        pass

    def test_mozilla(self):
        browser = 'mozilla'
        self.generic_method(browser)
        pass

    def test_edge(self):
        browser = 'edge'
        self.generic_method(browser)
        pass

    def generic_method(self, browser):
        self.driver = Driver(browser).get_driver()
        pass

    def tearDown(self):
        self.driver.close()

    @classmethod
    def tearDownClass(cls):
        if cls.driver is not None:
            cls.driver.quit()