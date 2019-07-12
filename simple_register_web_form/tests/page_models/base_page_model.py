from selenium.webdriver.common.by import By


class BasePageModel:

    def __init__(self, driver):
        self.driver = driver

    @property
    def url(self):
        '''
        returns root url
        :return:
        '''
        return 'http://demo.automationtesting.in/'

    @property
    def title(self):
        '''
        returns web page title
        :return:
        '''
        return self.driver.find_element(By.TAG_NAME, 'title')

