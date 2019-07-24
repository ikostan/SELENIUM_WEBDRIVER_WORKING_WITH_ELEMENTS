import unittest
from drivers.driver import Driver
import time
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = Driver('opera').get_driver()
        cls.test_url = 'https://www.ultimateqa.com/automation/'
        cls.test_title = 'Automation Practice - Ultimate QA'

    def test_opera_driver_works(self):

        # Open a web browser and maximize it
        self.driver.maximize_window()
        self.driver.get(self.test_url)

        # Explicit wait for page title
        WebDriverWait(self.driver, 20).until(expected_conditions.title_is(self.test_title))

        # get current url
        url = self.driver.current_url
        # get web page title
        title = self.driver.title

        self.assertEqual(self.test_url, url)
        self.assertEqual(self.test_title, title)

    def tearDown(self):
        self.driver.close()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

