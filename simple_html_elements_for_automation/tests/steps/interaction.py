from behave import *
from simple_html_elements_for_automation.tests.page_model.et_pb_section_1_page import SectionOnePageModel


use_step_matcher('re')


@when('I click on the button using ID')
def step_impl(context):
    '''
    Clicks on button that has ID
    :param context:
    :return:
    '''
    page = SectionOnePageModel(context.driver)
    page.button_with_id.click()
