from simple_html_elements_for_automation.tests.locators.button_success_locator import ButtonSuccessLocator


class ButtonSuccessPageModel:

    def __init__(self, driver):
        self.driver = driver

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
        return self.driver.find_element(*ButtonSuccessPageModel.MESSAGE)
