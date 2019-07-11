from behave import *
from selenium import webdriver
from config import chrome_web_driver_path
from simple_html_elements_for_automation.tests.page_model.button_success_page import ButtonSuccessPageModel
from simple_html_elements_for_automation.tests.page_model.et_pb_section_1_page import SectionOnePageModel


use_step_matcher('re')


@given('I am on the "Simple HTML Elements For Automation - Ultimate QA" page')
def step_impl(context):
    context.driver = webdriver.Chrome(chrome_web_driver_path)
    page = SectionOnePageModel(context.driver.maximize_window())
    context.driver.get(page.url)


@then('I am on the "Button success - Ultimate QA" page')
def step_impl(context):
    expected_url = ButtonSuccessPageModel(context.driver).url
    assert context.driver.current_url == expected_url

