import unittest
import time
from selenium.webdriver.common.by import By
from drivers.driver import Driver


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
        self.driver = None

    def test_chrome(self):
        browser = 'chrome'
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

    def test_ie(self):
        browser = 'ie'
        self.generic_method(browser)

    def generic_method(self, browser):

        # Open web browser and verify page title:
        self.driver = Driver(browser).get_driver()
        self.driver.maximize_window()
        self.driver.get(self.url)

        self.assertEqual(self.title, self.driver.title)

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

    def tearDown(self):
        self.driver.close()

    @classmethod
    def tearDownClass(cls):
        if cls.driver is not None:
            cls.driver.quit()
