import unittest
import datetime
from drivers.driver import Driver
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = None
        cls.test_url = ''
        cls.test_title = ''

    def setUp(self):
        if self.driver is not None:
            self.driver.quit()

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
        try:
            self.open_test_web_page(browser)


        except Exception as ec:
            print('\nERROR: {}'.format(ec))
            self.take_screen_shot()
            raise

    def open_test_web_page(self, browser):
        # Open test web page and verify URL + Title
        self.driver = Driver(browser).get_driver()
        self.driver.get(self.test_url)
        self.driver.maximize_window()

        WebDriverWait(self.driver, 15).until(expected_conditions.title_contains(self.test_title))
        time.sleep(1)

        self.assertEqual(self.test_url, self.driver.current_url)
        self.assertEqual(self.test_title, self.driver.title)

    def take_screen_shot(self):
        """Take a Screen-shot of the webpage when test Failed."""
        now = datetime.datetime.now()
        filename = 'screenshot-{}-{}.png'.format(self.driver.name,
                                                 datetime.datetime.strftime(now, '%Y-%m-%d_%H-%M-%S'))
        self.driver.save_screenshot(filename)
        print('\nScreenshot saved as {}'.format(filename))

    def screenshots_collector(self):
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
        folder_name = '{}\\screenshots_{}_{}'.format(screenshots_folder,
                                                     self.driver.name,
                                                     datetime.datetime.strftime(now, '%Y-%m-%d_%H-%M-%S'))

        files = os.listdir(os.curdir)
        for file in files:
            if '.png' in str(file):
                if not os.path.exists(os.curdir + '\\' + folder_name):
                    os.mkdir(folder_name)
                shutil.move(file.split('\\')[-1], os.curdir + '\\' + folder_name)

    def tearDown(self):
        self.screenshots_collector()
        self.driver.stop_client()
        self.driver.close()
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        if cls.driver is not None:
            cls.driver.quit()
