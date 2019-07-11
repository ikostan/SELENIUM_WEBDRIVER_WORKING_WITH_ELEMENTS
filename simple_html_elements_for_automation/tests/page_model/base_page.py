from simple_html_elements_for_automation.tests.locators.et_pb_base_page_locator import EtPbBasePageLocator


class EtPbBasePageModel:

    def __init__(self, driver):
        self.driver = driver

    @property
    def url(self):
        '''
        returns webpage url
        :return:
        '''
        return 'https://www.ultimateqa.com/simple-html-elements-for-automation/'

    @property
    def title(self):
        '''
        returns webpage title
        :return:
        '''
        return self.driver.find_element(*EtPbBasePageLocator.TITLE)
