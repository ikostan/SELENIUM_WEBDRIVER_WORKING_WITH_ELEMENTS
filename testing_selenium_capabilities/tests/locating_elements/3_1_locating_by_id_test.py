import unittest
import time
from drivers.driver import Driver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        cls.driver = None
        cls.test_url = 'http://automationpractice.com/index.php'
        cls.search_id = 'search_query_top'
        cls.test_title = 'My Store'
        cls.search_item = 'shirt'
        cls.search_btn_name = 'submit_search'

        cls.search_title = 'Search - My Store'
        cls.expected_search_result = 'SEARCH "SHIRT" \n1 result has been found.'
        cls.search_title_xpath = '/html/body/div/div[2]/div/div[3]/div[2]/h1'

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
        self.open_test_web_page(browser)

        # test for non existing item
        with self.assertRaises(NoSuchElementException):
            self.driver.find_element(By.ID, 'noname')

        # allocate search field
        search = self.driver.find_element(By.ID, self.search_id)

        # verify that search field is empty
        self.assertEqual('', search.get_attribute('value'))

        # enter search item and verify field value
        search.send_keys(self.search_item)
        self.assertEqual(self.search_item, search.get_attribute('value'))

        # hit on search button
        search_btn = self.driver.find_element(By.NAME, self.search_btn_name)
        search_btn.click()

        # wait till search page is loaded
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,
                                                                                              self.search_title_xpath)))
        time.sleep(1)
        search_header = self.driver.find_element(By.XPATH,
                                                 self.search_title_xpath)

        # Verify search results
        # \xa0 is actually non-breaking space in Latin1 (ISO 8859-1), also chr(160).
        # You should replace it
        result = search_header.text.replace(u'\xa0', u'')
        self.assertListEqual(list(self.expected_search_result.lower().split()),
                             list(result.strip().lower().split()))

    def open_test_web_page(self, browser):
        # Open test web page and verify URL + Title
        self.driver = Driver(browser).get_driver()
        self.driver.get(self.test_url)
        self.driver.maximize_window()
        time.sleep(1)
        self.assertEqual(self.test_url, self.driver.current_url)
        self.assertEqual(self.test_title, self.driver.title)

    def tearDown(self):
        self.driver.close()

    @classmethod
    def tearDownClass(cls):
        if cls.driver is not None:
            cls.driver.quit()
