import unittest
from drivers.driver import Driver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = None
        cls.test_url = 'https://www.seleniumeasy.com/test/'
        cls.test_title = 'Selenium Easy - Best Demo website to practice Selenium Webdriver Online'

        cls.simple_form_demo_xpath = '/html/body/div[3]/div/div[1]/div/div[2]/ul/li/ul/li[1]/ul/li[1]/a'
        cls.form_demo_title = 'Selenium Easy Demo - Simple Form to Automate using Selenium'

        cls.check_box_demo_xpath = '/html/body/div[2]/div/div[1]/div/div[2]/ul/li/ul/li[1]/ul/li[2]/a'
        cls.check_box_demo_title = 'Selenium Easy - Checkbox demo for automation using selenium'

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

        # Open test web site
        self.driver = Driver(browser).get_driver()
        self.driver.maximize_window()
        self.driver.get(self.test_url)
        self.assertEqual(self.test_url, self.driver.current_url)
        self.assertEqual(self.test_title, self.driver.title)

        # Go to main menu and expand it
        self.driver.find_element(By.XPATH,
                                 '/html/body/div[3]/div/div[1]/div/div[2]/ul/li/ul/li[1]/a').click()
        time.sleep(1)

        # open simple form demo page
        simple_form_menu_item = WebDriverWait(self.driver, 10).\
            until(expected_conditions.presence_of_element_located((By.XPATH,
                                                                   self.simple_form_demo_xpath)))
        simple_form_menu_item.click()
        time.sleep(1)
        self.assertEqual(self.form_demo_title, self.driver.title)

        # open check box demo page
        self.driver.find_element(By.XPATH,
                                 '/html/body/div[2]/div/div[1]/div/div[2]/ul/li/ul/li[1]/a').click()
        check_box_demo = WebDriverWait(self.driver, 10).\
            until(expected_conditions.presence_of_element_located((By.XPATH,
                                                                   self.check_box_demo_xpath)))
        check_box_demo.click()
        time.sleep(1)
        self.assertEqual(self.check_box_demo_title, self.driver.title)

        # Go back to simple form demo page:
        self.driver.back()
        time.sleep(1)
        self.assertEqual(self.form_demo_title, self.driver.title)

        # Go back to main page:
        self.driver.back()
        time.sleep(1)
        self.assertEqual(self.test_title, self.driver.title)

        # Go forward to simple form demo page
        self.driver.forward()
        time.sleep(1)
        self.assertEqual(self.form_demo_title, self.driver.title)

        # Go forward to check box demo page
        self.driver.forward()
        time.sleep(1)
        self.assertEqual(self.check_box_demo_title, self.driver.title)

    def tearDown(self):
        self.driver.close()

    @classmethod
    def tearDownClass(cls):
        if cls.driver is not None:
            cls.driver.quit()
