import unittest
import time
from drivers.driver import Driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait, TimeoutException
from selenium.webdriver.support import expected_conditions


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = None
        cls.url = 'http://demo.automationtesting.in/Frames.html'
        cls.window_name = 'Frames'

        cls.text_field_xpath = '/html/body/section/div/div/div/input'

        cls.single_iframe_btn_xpath = '/html/body/section/div[1]/div/div/div/div[1]/div/ul/li[1]/a'
        cls.single_iframe_id = 'singleframe'

        cls.multiple_iframes_btn_xpath = '/html/body/section/div[1]/div/div/div/div[1]/div/ul/li[2]/a'
        cls.multiple_frames_xpath = '/html/body/section/div[1]/div/div/div/div[2]/div[2]/iframe'
        cls.single_inside_multiple_iframe_xpath = '/html/body/section/div/div/iframe'

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

        self.open_web_browser(browser)

        # detect button
        single_iframe_btn = self.driver.find_element(By.XPATH, self.single_iframe_btn_xpath)

        # Click on 'Single iframe' button >>>
        # enter single iframe >>>
        single_iframe_btn.click()
        single_iframe = self.driver.find_element(By.ID, self.single_iframe_id)
        self.driver.switch_to.frame(single_iframe)

        # write text (single iframe) inside text field >>>
        # exit iframe
        txt_field = self.driver.find_element(By.XPATH, self.text_field_xpath)
        txt_field.send_keys('single iframe')
        time.sleep(1)
        self.assertEqual('single iframe', txt_field.get_attribute('value'))
        self.driver.switch_to.default_content()

        # detect button + click on it
        multiple_iframes_btn = self.driver.find_element(By.XPATH, self.multiple_iframes_btn_xpath)
        multiple_iframes_btn.click()

        # detect + switch to multiple iframe
        # implemented with wait due to slow performance of IE and FireFox
        wait = WebDriverWait(self.driver, 5)

        try:
            wait.until(expected_conditions.frame_to_be_available_and_switch_to_it(self.driver.find_element(By.XPATH,
                                                                                  self.multiple_frames_xpath)))
        except TimeoutException as ec:
            print('\n', ec)
            print('\nTrying to refresh...')
            self.driver.refresh()
            wait.until(expected_conditions.frame_to_be_available_and_switch_to_it(self.driver.find_element(By.XPATH,
                                                                                  self.multiple_frames_xpath)))

        # detect inner frame + switch to it
        inner_frame = self.driver.find_element(By.XPATH, self.single_inside_multiple_iframe_xpath)
        self.driver.switch_to.frame(inner_frame)

        # write text (single iframe) inside text field >>>
        # exit iframe
        try:
            WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH,
                                                                                             self.text_field_xpath)))
        except TimeoutException as ec:
            print('\n', ec)
            self.driver.switch_to.default_content()

            # detect inner frame + switch to it
            self.driver.switch_to.frame(inner_frame)
            WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH,
                                                                                             self.text_field_xpath)))

        txt_field = self.driver.find_element(By.XPATH, self.text_field_xpath)

        txt_field.send_keys('inner iframe')
        time.sleep(1)
        self.assertEqual('inner iframe', txt_field.get_attribute('value'))
        self.driver.switch_to.default_content()

        # click on iframe buttons back and forward:
        single_iframe_btn.click()
        time.sleep(1)
        multiple_iframes_btn.click()
        time.sleep(1)

    def open_web_browser(self, browser):

        try:
            # Launch webdriver on test web page + maximize window:
            self.driver = Driver(browser).get_driver()
            self.driver.get(self.url)
            self.driver.maximize_window()
            WebDriverWait(self.driver, 5).until(expected_conditions.title_is(self.window_name))
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
                    WebDriverWait(self.driver, 5).until(expected_conditions.title_is(self.window_name))
                except TimeoutException as ec:
                    print('\n', ec)
                    is_loaded = False

        finally:
            # Verify page title + url
            self.assertEqual(self.url, self.driver.current_url)
            self.assertEqual(self.window_name, self.driver.title)

    def tearDown(self):
        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)
            self.driver.stop_client()
            self.driver.close()
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        if cls.driver is not None:
            cls.driver.quit()
