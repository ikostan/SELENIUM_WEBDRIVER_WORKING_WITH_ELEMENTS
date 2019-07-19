import time
import unittest
from drivers.driver import Driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = None
        cls.test_url = 'http://newtours.demoaut.com/'
        cls.test_title = 'Welcome: Mercury Tours'
        cls.login_btn_name = 'login'

        cls.test_login_url = 'http://newtours.demoaut.com/mercurysignon.php'
        cls.test_login_title = 'Sign-on: Mercury Tours'

    def setUp(self):
        self.driver = None

    def test_chrome(self):
        browser = 'chrome'
        self.generic_method(browser)

    def test_ie(self):
        browser = 'ie'
        self.generic_method(browser)

    def test_opera(self):
        browser = 'opera'
        self.generic_method(browser)

    def test_mozilla(self):
        browser = 'mozilla'
        self.generic_method(browser)

    def test_edge(self):
        browser = 'edge'
        self.generic_method(browser)

    def generic_method(self, browser):

        # Allocate LOGIN button and click on it
        self.open_test_web_page(browser)
        login_btn = self.driver.find_element(By.NAME, self.login_btn_name)
        login_btn.click()
        time.sleep(1)

        # wait up to 10 secs for the url to change or else `TimeOutException` is raised.
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.title_is(self.test_login_title))

        # Verify that you are on the LOGIN web page
        new_url = self.driver.current_url
        self.assertTrue(self.test_url in new_url)
        self.assertEqual(self.test_login_title, self.driver.title)
        time.sleep(1)

        # Try to allocate non existing object
        with self.assertRaises(NoSuchElementException):
            self.driver.find_element(By.NAME, 'some_name')

    def open_test_web_page(self, browser):

        # Open test web page and verify URL + Title
        self.driver = Driver(browser).get_driver()
        self.driver.get(self.test_url)
        self.driver.maximize_window()
        time.sleep(1)
        self.assertEqual(self.test_url, self.driver.current_url)
        self.assertEqual(self.test_title, self.driver.title)

    def tearDown(self):
        self.driver.close()

    @classmethod
    def tearDownClass(cls):
        if cls.driver is not None:
            cls.driver.quit()