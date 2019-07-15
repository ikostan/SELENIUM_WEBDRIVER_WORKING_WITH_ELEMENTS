import unittest
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from drivers.driver import Driver


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = None
        cls.test_url = "https://www.google.com/doodles/"
        cls.id = 'passwd-id'
        cls.name = 'passwd'
        cls.xpath = '//input[@id=\'passwd-id\']'
        cls.search_field_name = 'q'

    def setUp(self):
        self.driver = None

    def test_chrome(self):
        browser = 'chrome'
        self.using_find_element_func(browser)

    def test_ie(self):
        browser = 'ie'
        self.using_find_element_func(browser)

    def test_edge(self):
        browser = 'edge'
        self.using_find_element_func(browser)

    def test_opera(self):
        browser = 'opera'
        self.using_find_element_func(browser)

    def test_mozilla(self):
        browser = 'mozilla'
        self.using_find_element_func(browser)

    def using_find_element_func(self, browser):

        self.driver = Driver(browser).get_driver()
        self.driver.maximize_window()
        self.driver.get(self.test_url)

        # 1. find element by id.
        # If nothing can be found, a NoSuchElementException will be raised.
        with self.assertRaises(NoSuchElementException):
            self.driver.find_element_by_id(self.id)

        # 2. find element by name.
        # If nothing can be found, a NoSuchElementException will be raised.
        with self.assertRaises(NoSuchElementException):
            self.driver.find_element_by_name(self.name)

        # 3. find element by xpath.
        # If nothing can be found, a NoSuchElementException will be raised.
        with self.assertRaises(NoSuchElementException):
            self.driver.find_element_by_xpath(self.xpath)

        # 4. Send keys.
        # It is possible to call send_keys on any element,
        # which makes it possible to test keyboard shortcuts such as those used on GMail.
        search_field = self.driver.find_element_by_name(self.search_field_name)
        search_field.send_keys('python')
        time.sleep(2)
        search_field.send_keys(" and some", Keys.ARROW_LEFT)
        time.sleep(2)
        search_field.send_keys(" and some", Keys.ARROW_RIGHT)
        time.sleep(2)
        # You can easily clear the contents of a text field
        # or textarea with the clear method
        search_field.clear()

    def tearDown(self):
        self.driver.close()

    @classmethod
    def tearDownClass(cls):
        if cls.driver is not None:
            cls.driver.quit()
