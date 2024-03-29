from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait, TimeoutException
from selenium.webdriver.support import expected_conditions
from drivers.driver import Driver
import unittest
import time


class SimpleUsage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        cls.driver = None
        cls.test_url = "http://www.python.org"
        cls.test_name = 'q'
        cls.test_str = "pycon"
        cls.text_message = "No results found."
        cls.test_title = "Welcome to Python.org"

    def setUp(self):
        if self.driver is not None:
            self.driver.quit()

        self.driver = None

    def test_chrome(self):
        self.simple_usage_generic_method('chrome')

    def test_edge(self):
        self.simple_usage_generic_method('edge')

    def test_ie(self):
        self.simple_usage_generic_method('ie')

    def test_mozilla(self):
        self.simple_usage_generic_method('mozilla')

    def test_opera(self):
        self.simple_usage_generic_method('opera')

    def simple_usage_generic_method(self, browser_name):

        try:
            self.driver = Driver(browser_name).get_driver()  # create a drivers object
            self.driver.get(self.test_url)  # open web browser on test web page
            self.driver.maximize_window()
            WebDriverWait(self.driver, 15).until(expected_conditions.title_is(self.test_title))
        except TimeoutException as ec:
            print('\n', ec)

            is_loaded = False
            while not is_loaded:
                is_loaded = True
                try:
                    self.tearDown()
                    self.driver = Driver(browser_name).get_driver()  # create a drivers object
                    self.driver.get(self.test_url)  # open web browser on test web page
                    self.driver.maximize_window()
                    WebDriverWait(self.driver, 15).until(expected_conditions.title_is(self.test_title))
                except TimeoutException as ec:
                    print('\n', ec)
                    is_loaded = False

        assert self.test_title in self.driver.title  # verify webpage title

        elem = self.driver.find_element_by_name(self.test_name)  # finds HTML element by name
        elem.clear()  # clear the field

        elem.send_keys(self.test_str)  # type test string in the search field
        elem.send_keys(Keys.RETURN)  # press ENTER
        assert self.text_message not in self.driver.page_source  # look for test message

    def tearDown(self):
        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)
            self.driver.stop_client()
            self.driver.close()
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        if cls.driver is not None:
            cls.driver.quit()
