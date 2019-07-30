import unittest
import datetime
from drivers.driver import Driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = None
        cls.test_url = 'http://automationpractice.com/index.php'
        cls.test_title = 'My Store'

        cls.css_selector = '#block_top_menu > ul > li:nth-child(3) > a'
        cls.t_shirts_text = 'T-shirts'
        cls.t_shirts_link = "http://automationpractice.com/index.php?id_category=5&controller=category"
        cls.t_shirts_title = 'T-shirts - My Store'

    def setUp(self):
        if self.driver is not None:
            self.driver.quit()

        self.driver = None

    # @unittest.skip('not ready')
    def test_chrome(self):
        browser = 'chrome'
        self.generic_method(browser)

    # @unittest.skip('not ready')
    def test_ie(self):
        browser = 'ie'
        self.generic_method(browser)

    # @unittest.skip('not ready')
    def test_opera(self):
        browser = 'opera'
        self.generic_method(browser)

    # @unittest.skip('not ready')
    def test_mozilla(self):
        browser = 'mozilla'
        self.generic_method(browser)

    # @unittest.skip('not ready')
    def test_edge(self):
        browser = 'edge'
        self.generic_method(browser)

    def generic_method(self, browser):
        try:
            self.open_test_web_page(browser)

            t_shirts_btn = WebDriverWait(self.driver,
                                         10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                                               self.css_selector)))
            t_shirts_btn.click()
            WebDriverWait(self.driver,
                          10).until(EC.title_contains(self.t_shirts_title))
            self.assertEqual(self.t_shirts_title, self.driver.title)
            self.assertEqual(self.t_shirts_link, self.driver.current_url)

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
