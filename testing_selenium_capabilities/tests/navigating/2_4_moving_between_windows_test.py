import unittest
import time
import datetime
from drivers.driver import Driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait, TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import WebDriverException


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = None
        cls.url = 'http://demo.automationtesting.in/Windows.html'
        cls.new_url = 'http://www.sakinalium.in/'
        cls.origin_window_name = 'Frames & windows'
        cls.new_window_name = 'Sakinalium | Home'

    def setUp(self):
        if self.driver is not None:
            self.driver.quit()

        self.driver = None

    def test_chrome(self):
        browser = 'chrome'
        try:
            self.generic_method(browser)
        except Exception:
            self.take_screen_shot()
            raise

    def test_ie(self):
        browser = 'ie'
        try:
            self.generic_method(browser)
        except Exception:
            self.take_screen_shot()
            raise

    def test_opera(self):
        browser = 'opera'
        try:
            self.generic_method(browser)
        except Exception:
            self.take_screen_shot()
            raise

    def test_mozilla(self):
        browser = 'mozilla'
        try:
            self.generic_method(browser)
        except Exception:
            self.take_screen_shot()
            raise

    def test_edge(self):
        browser = 'edge'
        try:
            self.generic_method(browser)
        except Exception:
            self.take_screen_shot()
            raise

    def generic_method(self, browser):

        self.open_web_browser(browser)

        # Get current window handle:
        main_window = self.driver.current_window_handle

        try:
            # Hit on click button and switch to new window:
            btn = WebDriverWait(self.driver, 5).until(
                expected_conditions.element_to_be_clickable((By.XPATH,
                                                             '/html/body/div[1]/div/div/div/div[2]/div[1]/a/button')))
            btn.click()
            time.sleep(1)

            # New tabs will be the last object in window_handles:
            self.driver.switch_to.window(self.driver.window_handles[-1])
            self.driver.maximize_window()
        except WebDriverException as ec:
            print('\n', ec)
            self.screen_shot()
            raise

        # Wait for element to appear.
        # Implemented due to a very slow performance of IE and FireFox.
        try:
            WebDriverWait(self.driver, 5).until(expected_conditions.title_is(self.new_window_name))
        except TimeoutException as ec:
            is_loaded = False

            while not is_loaded:
                is_loaded = True
                try:
                    print('\n', ec)
                    self.driver.close()
                    time.sleep(1)
                    self.driver.switch_to.window(main_window)
                    btn.click()
                    self.driver.switch_to.window(self.driver.window_handles[-1])
                    self.driver.maximize_window()
                    WebDriverWait(self.driver, 5).until(expected_conditions.title_is(self.new_window_name))
                except WebDriverException as ec:
                    print('\n', ex)
                    is_loaded = False

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

    def open_web_browser(self, browser):
        try:
            # Launch webdriver on test web page + maximize window:
            self.driver = Driver(browser).get_driver()
            self.driver.get(self.url)
            self.driver.maximize_window()
            WebDriverWait(self.driver, 5).until(expected_conditions.title_is(self.origin_window_name))

        except TimeoutException as ec:
            print('\n', ec)
            is_loaded = False
            while not is_loaded:
                is_loaded = True
                try:
                    self.tearDown()
                    self.driver = Driver(browser).get_driver()
                    self.driver.get(self.url)
                    self.driver.maximize_window()
                    WebDriverWait(self.driver, 5).until(expected_conditions.title_is(self.origin_window_name))
                except TimeoutException as ec:
                    print('\n', ec)
                    is_loaded = False

        finally:
            self.assertEqual(self.url, self.driver.current_url)
            self.assertEqual(self.origin_window_name, self.driver.title)

    def screen_shot(self):
        """Take a Screen-shot of the webpage when test Failed."""
        now = datetime.datetime.now()
        filename = 'screenshot-{}-{}.png'.format(self.driver.name, datetime.datetime.strftime(now, '%Y-%m-%d_%H-%M-%S'))
        self.driver.save_screenshot(filename)
        print('\nScreenshot saved as {}'.format(filename))

    @staticmethod
    def screenshots_collector():
        '''
        Collect all screenshots and put them into screenshots directory
        :return:
        '''
        import os
        import shutil

        screenshots_folder = 'screenshots'
        if not os.path.exists(os.curdir + '\\screenshots'):
            os.mkdir(screenshots_folder)

        now = datetime.datetime.now()
        folder_name = '{}\\screenshots_{}'.format(screenshots_folder, datetime.datetime.strftime(now, '%Y-%m-%d_%H-%M-%S'))

        files = os.listdir(os.curdir)
        for file in files:
            if '.png' in str(file):
                if not os.path.exists(os.curdir + '\\' + folder_name):
                    os.mkdir(folder_name)
                shutil.move(file.split('\\')[-1], os.curdir + '\\' + folder_name)

    def tearDown(self):
        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)
            self.driver.stop_client()
            self.driver.close()
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        cls.screenshots_collector()
        if cls.driver is not None:
            cls.driver.quit()
