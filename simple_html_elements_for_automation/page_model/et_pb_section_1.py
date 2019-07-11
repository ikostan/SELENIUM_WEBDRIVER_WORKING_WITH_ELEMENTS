from simple_html_elements_for_automation.locators.et_pb_section_1_locator import EtPbSection1
from simple_html_elements_for_automation.page_model.base_page import EtPbBasePage


class SectionOne(EtPbBasePage):

    @property
    def url(self):
        '''
        returns webpage url
        :return:
        '''
        return super(SectionOne, self).url

    # Click this button using "ID"
    # Click me using this link text!
    # Click me using this link text
    # Click button using ClassName
    # Click button using Name

