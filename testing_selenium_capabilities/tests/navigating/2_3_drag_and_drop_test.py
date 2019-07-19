import unittest
import time
from drivers.driver import Driver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = None
        cls.test_url = 'https://jqueryui.com/droppable/'

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
        self.driver = Driver(browser).get_driver()
        self.driver.get(self.test_url)
        self.driver.maximize_window()

        self.assertEqual(self.test_url, self.driver.current_url)

        iframe = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/iframe')
        self.driver.switch_to.frame(iframe)

        source = self.driver.find_element_by_xpath('//*[@id="draggable"]')
        target = self.driver.find_element_by_id('droppable')
        self.assertEqual("Drop here", target.text)
        time.sleep(2)

        actions = ActionChains(self.driver)
        actions.drag_and_drop(source, target).perform()

        self.assertEqual("Dropped!", target.text)
        time.sleep(2)

    def tearDown(self):
        self.driver.close()

    @classmethod
    def tearDownClass(cls):
        if cls.driver is not None:
            cls.driver.quit()
