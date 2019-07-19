import unittest
import time
from drivers.driver import Driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = None
        cls.url = 'http://demo.automationtesting.in/Windows.html'
        cls.new_url = 'http://www.sakinalium.in/'
        cls.origin_window_name = 'Frames & windows'
        cls.new_window_name = 'Sakinalium | Home'

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

        # Launch webdriver on test web page + maximize window:
        self.driver = Driver(browser).get_driver()
        self.driver.get(self.url)
        self.driver.maximize_window()

        # Get current window handle:
        main_window = self.driver.current_window_handle

        # Hit on click button and switch to new window:
        self.driver.find_element(By.XPATH,
                                 '/html/body/div[1]/div/div/'
                                 'div/div[2]/div[1]/a/button').click()

        # New tabs will be the last object in window_handles:
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.driver.maximize_window()

        # Wait for element to appear.
        # Implemented due to a very slow performance of IE and FireFox.
        wait = WebDriverWait(self.driver, 10)
        wait.until(ec.title_is(self.new_window_name))

        # Verify new tab name + url:
        self.assertEqual(self.new_window_name, self.driver.title)
        self.assertEqual(self.new_url, self.driver.current_url)
        time.sleep(1)

        # Get a new window handle:
        new_window = self.driver.current_window_handle

        # Switch back to original window:
        self.driver.switch_to.window(main_window)
        self.assertEqual(self.origin_window_name, self.driver.title)
        self.assertEqual(self.url, self.driver.current_url)
        time.sleep(1)

        # Switch to a new tab:
        self.driver.switch_to.window(new_window)
        self.assertEqual(self.new_window_name, self.driver.title)
        self.assertEqual(self.new_url, self.driver.current_url)
        time.sleep(1)

    def tearDown(self):
        self.driver.quit()

    @classmethod
    def tearDownClass(cls):
        if cls.driver is not None:
            cls.driver.quit()
