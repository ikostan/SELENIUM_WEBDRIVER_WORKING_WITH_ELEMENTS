import datetime
from selenium.webdriver.support.events import AbstractEventListener


class ScreenshotListener(AbstractEventListener):
    '''
    Automatically capture browser screenshots after failed Selenium Python tests
    Source: http://blog.likewise.org/2015/01/automatically-capture-browser-screenshots-after-failed-python-ghostdriver-tests/
    '''

    def on_exception(self, exception, driver):
        """Take a Screen-shot of the webpage when test Failed."""
        now = datetime.datetime.now()
        filename = 'screenshot-{}-{}.png'.format(driver.name, datetime.datetime.strftime(now, '%Y-%m-%d_%H-%M-%S'))
        driver.save_screenshot(filename)
        print('\nScreenshot saved as {}'.format(filename))
