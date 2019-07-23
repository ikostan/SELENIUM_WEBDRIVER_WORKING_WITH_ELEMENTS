from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from drivers.driver import Driver
import unittest


# The test case class is inherited from unittest.TestCase.
# Inheriting from TestCase class is the way to tell unittest module
# that this is a test case:
class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        '''
        Runs only one time before all test method
        :return:
        '''

        cls.driver = Driver('chrome').get_driver()

    def setUp(self):
        '''
        The setUp is part of initialization, this method will get called before
        every test function which you are going to write in this test case class.
        :return:
        '''
        self.test_url = "http://www.python.org"
        self.test_name = 'q'
        self.test_str = "pycon"
        self.text_message = "No results found."
        self.test_title = "Python"

    def test_something(self):
        '''
        This is the test case method.
        The test case method should always start with characters test.
        :return:
        '''

        # The driver.get method will navigate to a page given by the URL.
        # WebDriver will wait until the page has fully loaded
        # (that is, the “onload” event has fired) before returning
        # control to your test or script.
        self.driver.get(self.test_url)

        # maximize browser window
        self.driver.maximize_window()

        # An assertion to confirm that title has “Python” word in it:
        self.assertIn(self.test_title, self.driver.title)

        # WebDriver offers a number of ways to find elements
        # using one of the find_element_by_* methods.
        element = self.driver.find_element(By.NAME, self.test_name)

        # Next, we are sending keys, this is similar to entering keys using your keyboard.
        # Special keys can be send using Keys class imported from
        # selenium.webdriver.common.keys:
        element.send_keys(self.test_str)  # writing text inside HTML object
        element.send_keys(Keys.RETURN)  # press ENTER

        # After submission of the page, you should get the result
        # as per search if there is any. To ensure that some results are found,
        # make an assertion:
        self.assertFalse(self.text_message in self.driver.page_source)

    def tearDown(self):
        '''
        runs after each test method
        :return:
        '''
        self.driver.close()

    @classmethod
    def tearDownClass(cls):
        '''
        runs only one time after all test methods
        :return:
        '''
        if cls.driver is not None:
            cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
