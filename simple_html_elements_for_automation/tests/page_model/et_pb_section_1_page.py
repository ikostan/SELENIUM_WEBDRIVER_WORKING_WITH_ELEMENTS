from simple_html_elements_for_automation.tests.page_model.base_page import EtPbBasePageModel
from simple_html_elements_for_automation.tests.locators.et_pb_section_1_locator import EtPbSection1Locator


class SectionOnePageModel(EtPbBasePageModel):

    @property
    def url(self):
        '''
        returns webpage url
        :return:
        '''
        return super(SectionOnePageModel, self).url

    # Click this button using "ID"
    @property
    def button_with_id(self):
        '''
        returns button by ID
        :return:
        '''
        return self.driver.find_element(*EtPbSection1Locator.BUTTON_WITH_ID)

    # Click me using this link text!
    # Click me using this link text
    # Click button using ClassName
    # Click button using Name

