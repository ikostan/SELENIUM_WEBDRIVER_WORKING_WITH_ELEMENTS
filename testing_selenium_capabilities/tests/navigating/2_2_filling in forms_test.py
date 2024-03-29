import unittest
import time
import datetime
from selenium.webdriver.common.by import By
from drivers.driver import Driver
from selenium.webdriver.support.wait import WebDriverWait, TimeoutException
from selenium.webdriver.support import expected_conditions


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.url = 'https://accounts.google.com/signup/v2/webcreateaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&hl=en-GB&flowName=GlifWebSignIn&flowEntry=SignUp'
        cls.driver = None
        cls.title = 'Create your Google Account'
        cls.field_name = ['firstName', 'lastName', 'Username', 'Passwd', 'ConfirmPasswd']
        cls.user_account = {
            'firstName': 'John',
            'lastName': 'Snow',
            'Username': 'the_king_of_the_north',
            'Passwd': 'The1AndOnly!',
            'ConfirmPasswd': 'The1AndOnly!'
        }

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

    def test_ie(self):
        browser = 'ie'
        self.generic_method(browser)

    def generic_method(self, browser):

        self.open_web_browser(browser)

        # Set predefine value for each field from
        # 'Create your Google Account' registration form:
        for name in self.field_name:
            element = self.driver.find_element_by_name(name)
            element.clear()
            element.send_keys(self.user_account[name])

        # Verify all entered values:
        for name in self.field_name:
            expected = self.user_account[name]
            actual = self.driver.find_element_by_name(name).get_attribute('value')
            # print('expected: {}, actual: {}'.format(expected, actual))  # debug only
            self.assertEqual(expected, actual)

        # click on aye button in order to make
        # 'Confirm' field value visible:
        is_pswd_visible_btn = self.driver.find_element(By.XPATH,
                                                       '/html/body/div[1]/div/div[2]/'
                                                       'div[1]/div[2]/form/div[2]/div/'
                                                       'div[1]/div[3]/div[2]/div')

        # verify that 'Confirm' field value is visible:
        expected = 'password'
        actual = self.driver.find_element_by_name(self.field_name[-1]).get_attribute("type")
        self.assertEqual(expected, actual)
        time.sleep(1)

        # click on aye button in order to make
        # 'Confirm' field value encrypted:
        is_pswd_visible_btn.click()

        # verify that 'Confirm' field value is visible:
        expected = 'text'
        actual = self.driver.find_element_by_name(self.field_name[-1]).get_attribute("type")
        self.assertEqual(expected, actual)
        time.sleep(1)

        # click on aye button in order to make
        # 'Confirm' field value encrypted:
        is_pswd_visible_btn.click()

        # verify that 'Confirm' field value is visible:
        expected = 'password'
        actual = self.driver.find_element_by_name(self.field_name[-1]).get_attribute("type")
        self.assertEqual(expected, actual)
        time.sleep(1)

    def take_screen_shot(self):
        """Take a Screen-shot of the webpage when test Failed."""
        now = datetime.datetime.now()
        filename = 'screenshot-{}-{}.png'.format(self.driver.name, datetime.datetime.strftime(now, '%Y-%m-%d_%H-%M-%S'))
        self.driver.save_screenshot(filename)
        print('\nScreenshot saved as {}'.format(filename))

    def open_web_browser(self, browser):
        try:
            # Open web browser and verify page title:
            self.driver = Driver(browser).get_driver()
            self.driver.get(self.url)
            self.driver.maximize_window()
            WebDriverWait(self.driver, 5).until(expected_conditions.title_contains(self.title))

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
                    WebDriverWait(self.driver, 5).until(expected_conditions.title_is(self.title))
                except TimeoutException as ec:
                    print('\n', ec)
                    is_loaded = False

        finally:
            self.assertEqual(self.url, self.driver.current_url)
            self.assertEqual(self.title, self.driver.title)

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
        folder_name = '{}\\screenshots_{}'.format(screenshots_folder,
                                                  datetime.datetime.strftime(now, '%Y-%m-%d_%H-%M-%S'))

        files = os.listdir(os.curdir)
        for file in files:
            if '.png' in str(file):
                if not os.path.exists(os.curdir + '\\' + folder_name):
                    os.mkdir(folder_name)
                shutil.move(file.split('\\')[-1], os.curdir + '\\' + folder_name)

    def tearDown(self):
        self.driver.stop_client()
        self.driver.close()
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        cls.screenshots_collector()
        if cls.driver is not None:
            cls.driver.quit()
