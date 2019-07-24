import unittest
import time
from drivers.driver import Driver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait, TimeoutException
from selenium.webdriver.support import expected_conditions


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = None
        cls.test_url = 'https://jqueryui.com/droppable/'
        cls.test_title = 'Droppable | jQuery UI'

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

        try:
            # Open web browser and verify page title:
            self.driver = Driver(browser).get_driver()
            self.driver.get(self.test_url)
            self.driver.maximize_window()
            WebDriverWait(self.driver, 20).until(expected_conditions.title_is(self.test_title))

        except TimeoutException as ec:
            print('\n', ec)
            is_loaded = False
            while not is_loaded:
                is_loaded = True
                try:
                    self.tearDown()
                    self.driver = Driver(browser).get_driver()
                    self.driver.get(self.test_url)
                    self.driver.maximize_window()
                    WebDriverWait(self.driver, 15).until(expected_conditions.title_is(self.test_title))
                except TimeoutException as ec:
                    print('\n', ec)
                    is_loaded = False

        finally:
            self.assertEqual(self.test_url, self.driver.current_url)
            self.assertEqual(self.test_title, self.driver.title)

        iframe = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/iframe')
        self.driver.switch_to.frame(iframe)

        source = self.driver.find_element_by_xpath('//*[@id="draggable"]')
        target = self.driver.find_element_by_id('droppable')
        self.assertEqual("Drop here", target.text)
        time.sleep(2)

        actions = ActionChains(self.driver)
        actions.drag_and_drop(source, target).perform()
        time.sleep(1)
        self.assertEqual("Dropped!", target.text)
        time.sleep(1)

    def tearDown(self):
        self.driver.stop_client()
        self.driver.close()
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        if cls.driver is not None:
            cls.driver.quit()
