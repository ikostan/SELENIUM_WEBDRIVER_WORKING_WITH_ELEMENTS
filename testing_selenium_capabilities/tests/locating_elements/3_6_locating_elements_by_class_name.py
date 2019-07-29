import unittest
import datetime
from drivers.driver import Driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = None
        cls.test_url = 'http://automationpractice.com/index.php'
        cls.test_title = 'My Store'
        cls.login_text = 'Sign in'

    def setUp(self):
        if self.driver is not None:
            self.driver.quit()

        self.driver = None

    # @unittest.skip('not ready')
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
            login = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'login')))
            self.assertEqual(self.logit_text, login.text)

        except Exception as ec:
            print('\nERROR: {}'.format(ec))
            self.take_screen_shot()
            raise

    def open_test_web_page(self, browser):
        # Open test web page and verify URL + Title
        self.driver = Driver(browser).get_driver()
        self.driver.get(self.test_url)
        self.driver.maximize_window()

        WebDriverWait(self.driver, 15).until(EC.title_contains(self.test_title))

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

    @classmethod
    def tearDownClass(cls):
        if cls.driver is not None:
            cls.driver.quit()
