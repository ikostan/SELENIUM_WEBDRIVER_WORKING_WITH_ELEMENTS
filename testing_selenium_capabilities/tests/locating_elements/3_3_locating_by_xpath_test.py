import unittest
from drivers.driver import Driver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait, TimeoutException
from selenium.webdriver.support import expected_conditions


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = None
        cls.test_title = 'PHPTRAVELS | Travel Technology Partner'
        cls.test_url = 'https://www.phptravels.net/'

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

        # open test webpage
        self.open_test_web_page(browser)

        # detect 'My Account' menu item and click on it:
        drop_down_menu = self.driver.find_element(By.XPATH,
                                                  '/html/body/nav/div/div[2]/ul[2]/ul/li[1]/a')
        drop_down_menu.click()

        # verify that submenu items are visible
        self.assertEqual('true', drop_down_menu.get_attribute('aria-expanded'))
        time.sleep(1)

        # Hit 'My Account' again and verify that submenu items are invisible
        drop_down_menu.click()
        self.assertEqual('false', drop_down_menu.get_attribute('aria-expanded'))
        time.sleep(1)

    def open_test_web_page(self, browser):
        # Open test web page and verify URL + Title
        try:
            self.driver = Driver(browser).get_driver()
            self.driver.get(self.test_url)
            self.driver.maximize_window()
            WebDriverWait(self.driver, 15).until(expected_conditions.title_is(self.test_title))

        except TimeoutException as ec:
            print('\n', ec)

            is_loaded = False
            while not is_loaded:
                is_loaded = True
                try:
                    self.tearDown()
                    self.driver = Driver(browser).get_driver()
                    self.driver.get(self.test_url)
                    self.driver.maximize_window()
                    WebDriverWait(self.driver, 15).until(expected_conditions.title_is(self.test_title))
                except TimeoutException as ec:
                    print('\n', ec)
                    is_loaded = False

        finally:
            self.assertEqual(self.test_url, self.driver.current_url)
            self.assertEqual(self.test_title, self.driver.title)

    def tearDown(self):
        self.driver.close()

    @classmethod
    def tearDownClass(cls):
        if cls.driver is not None:
            cls.driver.quit()
