from simple_html_elements_for_automation.locators.button_success import ButtonSuccessLocator


class ButtonSuccessLocator:

    def __init__(self, driver):
        self.driver

    @property
    def url(self):
        '''
        returns webpage url
        :return:
        '''
        return 'https://www.ultimateqa.com/button-success/'

    @property
    def title(self):
        '''
        returns webpage title
        :return:
        '''
        return self.driver.find_element(*ButtonSuccessLocator.TITLE)

    @property
    def message(self):
        '''
        returns webpage message
        :return:
        '''
        return self.driver.find_element(*ButtonSuccessLocator.MESSAGE)
