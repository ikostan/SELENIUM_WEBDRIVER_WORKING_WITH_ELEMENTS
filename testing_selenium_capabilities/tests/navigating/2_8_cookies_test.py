import unittest
from drivers.driver import Driver


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = None
        cls.test_url = "http://www.example.com/"
        cls.cookie = {'name': 'foo',
                      'value': 'bar'}
        cls.page_title_xpath = '/html/body/div/h1'

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

        # Go to the correct domain
        self.driver = Driver(browser).get_driver()
        self.driver.maximize_window()
        self.driver.get(self.test_url)
        self.assertEqual(self.test_url, self.driver.current_url)

        # Now set the cookie. This one's valid for the entire domain
        self.driver.add_cookie(self.cookie)

        # Verify the imported cookies
        self.assertTrue(self.cookie['name'] == self.driver.get_cookies()[0]['name'])
        self.assertTrue(self.cookie['value'] == self.driver.get_cookies()[0]['value'])

    def tearDown(self):
        self.driver.close()

    @classmethod
    def tearDownClass(cls):
        if cls.driver is not None:
            cls.driver.quit()
