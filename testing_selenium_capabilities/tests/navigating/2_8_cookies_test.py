import unittest
from drivers.driver import Driver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = None
        cls.test_title = 'Example Domain'
        cls.test_url = "http://www.example.com/"
        cls.cookie = {'name': 'foo',
                      'value': 'bar'}
        cls.page_title_xpath = '/html/body/div/h1'

    def setUp(self):
        if self.driver is not None:
            self.driver.quit()

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

        # Go to the correct domain
        self.driver = Driver(browser).get_driver()
        self.driver.get(self.test_url)
        self.driver.maximize_window()

        WebDriverWait(self.driver, 15).until(expected_conditions.title_contains(self.test_title))

        self.assertEqual(self.test_url, self.driver.current_url)

        # Now set the cookie. This one's valid for the entire domain
        self.driver.add_cookie(self.cookie)

        # Verify the imported cookies
        self.assertTrue(self.cookie['name'] == self.driver.get_cookies()[0]['name'])
        self.assertTrue(self.cookie['value'] == self.driver.get_cookies()[0]['value'])

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
