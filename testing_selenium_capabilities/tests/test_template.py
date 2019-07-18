import unittest
from drivers.driver import Driver
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = None

    def setUp(self):
        self.driver = None

    @unittest.skip('not ready')
    def test_chrome(self):
        browser = 'chrome'
        self.generic_method(browser)

    @unittest.skip('not ready')
    def test_ie(self):
        browser = 'ie'
        self.generic_method(browser)

    @unittest.skip('not ready')
    def test_opera(self):
        browser = 'opera'
        self.generic_method(browser)

    @unittest.skip('not ready')
    def test_mozilla(self):
        browser = 'mozilla'
        self.generic_method(browser)

    @unittest.skip('not ready')
    def test_edge(self):
        browser = 'edge'
        self.generic_method(browser)

    def generic_method(self, browser):
        self.open_test_web_page(browser)
        pass

    def open_test_web_page(self, browser):
        # Open test web page and verify URL + Title
        self.driver = Driver(browser).get_driver()
        self.driver.maximize_window()
        self.driver.get(self.test_url)
        time.sleep(1)
        self.assertEqual(self.test_url, self.driver.current_url)
        self.assertEqual(self.test_title, self.driver.title)

    def tearDown(self):
        self.driver.close()

    @classmethod
    def tearDownClass(cls):
        if cls.driver is not None:
            cls.driver.quit()
