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
        cls.jscript_alerts_url = 'https://www.seleniumeasy.com/test/javascript-alert-box-demo.html'
        cls.jscript_alerts_title = 'Selenium Easy Demo - Automate All Scenarios'

        cls.jscript_alert_box_btn_xpath = '/html/body/div[2]/div/div[2]/div[1]/div[2]/button'
        cls.jscript_confirm_box_xpath = '/html/body/div[2]/div/div[2]/div[2]/div[2]/button'
        cls.configrm_demo_id = 'confirm-demo'
        cls.jscript_alert_box_prompt_xpath = '/html/body/div[2]/div/div[2]/div[3]/div[2]/button'
        cls.promt_demo_id = 'prompt-demo'

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
        self.driver = Driver(browser).get_driver()
        self.driver.maximize_window()
        self.driver.get(self.jscript_alerts_url)

        if browser == "chrome":
            self.driver.refresh()

        try:
            WebDriverWait(self.driver, 20).until(expected_conditions.title_contains(self.jscript_alerts_title))
        except TimeoutException as ec:
            print(ec)
            print('\nTrying to refresh...')
            self.driver.refresh()
            WebDriverWait(self.driver, 20).until(expected_conditions.title_contains(self.jscript_alerts_title))

        # Verify URL + Title
        self.assertEqual(self.jscript_alerts_url, self.driver.current_url)
        self.assertEqual(self.jscript_alerts_title, self.driver.title)

        # Test Java Script Alert Box
        self.alert_box_testing()

        # Test Java Script Confirm Box
        self.confirm_box_testing()

        # Test Java Script Prompt Box
        self.prompt_box_testing()

    def alert_box_testing(self):

        # Open Java Script Alert Box
        self.driver.find_element(By.XPATH, self.jscript_alert_box_btn_xpath).click()
        alert_box = WebDriverWait(self.driver, 15).until(expected_conditions.alert_is_present())

        # Verify alert box text and close the alert
        self.assertEqual('I am an alert box!', alert_box.text)
        time.sleep(1)
        alert_box.accept()

        # Back to the main window
        self.driver.switch_to.default_content()

    def confirm_box_testing(self):

        # Open Java Script Confirm Box
        self.driver.find_element(By.XPATH, self.jscript_confirm_box_xpath).click()
        confirm_box = WebDriverWait(self.driver, 15).until(expected_conditions.alert_is_present())

        # Verify text >>> Hit OK button
        self.assertTrue('Press a button!' in confirm_box.text)
        time.sleep(1)
        confirm_box.accept()

        # Verify the result
        self.driver.switch_to.default_content()
        self.assertEqual('You pressed OK!', self.driver.find_element(By.ID, self.configrm_demo_id).text)
        time.sleep(1)

        # Open alert again
        self.driver.find_element(By.XPATH, self.jscript_confirm_box_xpath).click()
        confirm_box = WebDriverWait(self.driver, 15).until(expected_conditions.alert_is_present())

        # Verify text >>> Hit CANCEL button
        self.assertTrue('Press a button!' in confirm_box.text)
        time.sleep(1)
        confirm_box.dismiss()

        # Verify the result
        self.driver.switch_to.default_content()
        self.assertEqual('You pressed Cancel!', self.driver.find_element(By.ID, self.configrm_demo_id).text)
        time.sleep(1)

    def prompt_box_testing(self):

        # Open prompt box and verify prompt text
        self.driver.find_element(By.XPATH, self.jscript_alert_box_prompt_xpath).click()
        prompt_box = WebDriverWait(self.driver, 15).until(expected_conditions.alert_is_present())
        self.assertEqual('Please enter your name', prompt_box.text)
        time.sleep(1)

        # Cancel it and verify the result
        prompt_box.dismiss()
        self.driver.switch_to.default_content()
        self.assertEqual('', self.driver.find_element(By.ID, self.promt_demo_id).text)
        time.sleep(1)

        # Open prompt again
        self.driver.switch_to.default_content()
        self.driver.find_element(By.XPATH, self.jscript_alert_box_prompt_xpath).click()
        prompt_box = WebDriverWait(self.driver, 15).until(expected_conditions.alert_is_present())

        # Type name in prompt box
        time.sleep(1)
        prompt_box.send_keys('John Snow')
        time.sleep(1)

        # Accept it and verify text
        prompt_box.accept()
        self.driver.switch_to.default_content()
        self.assertEqual('You have entered \'John Snow\' !', self.driver.find_element(By.ID, self.promt_demo_id).text)
        time.sleep(1)

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
