from behave import given, when, then, step
from selenium import webdriver


driver = webdriver.Chrome


@step('Go to Tradecore')
def step_impl(context):
    context.driver.get("https://demo-biq.dev.tradecore.io/#/")

@step('Click Next')
def step_impl(context):
    context.driver.find_element_by_id("button-step").click()

@step('This field is required error')
def step_impl(context):
    assert context.driver.find_element_by_css_selector("[ng-message='required']").is_displayed()