from simple_html_elements_for_automation.tests.locators.et_pb_section_3_locator import EtPbSection3Locator
from simple_html_elements_for_automation.tests.page_model.base_page import EtPbBasePageModel


class EtPbSection3PageModel(EtPbBasePageModel):

    @property
    def url(self):
        '''
        returns webpage url
        :return:
        '''
        return super(EtPbSection3PageModel, self).url

    @property
    def first_btn(self):
        '''
        returns all buttons with the same xpath
        :return:
        '''
        pass


