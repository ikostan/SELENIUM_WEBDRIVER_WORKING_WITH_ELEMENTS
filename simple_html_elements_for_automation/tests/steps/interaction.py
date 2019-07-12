from behave import *
from simple_html_elements_for_automation.tests.page_model.et_pb_section_1_page import SectionOnePageModel
from simple_html_elements_for_automation.tests.page_model.et_pb_section_3_page import EtPbSection3PageModel


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


@step("I can identify first Xpath button")
def step_impl(context):
    page = EtPbSection3PageModel(context.driver)
    print('{}'.format(len(page.first_btn)))
    assert len(page.x_path_btns) == 1


@when('I click on the first one')
def step_impl(context):
    page = EtPbSection3PageModel(context.driver)
    page.x_path_btns[0].click()
