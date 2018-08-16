from behave import given, when, then
from selenium import webdriver


driver = webdriver.Chrome


@given(u'Go to Tradecore')
def step_impl(context):
    #driver.get("https://demo-biq.dev.tradecore.io/#/")
    pass

@when(u'Click Next')
def step_impl(context):
    #driver.find_element_by_id("button-step").click()
    pass

@then(u'This field is required error')
def step_impl(context):
    #assert driver.find_element_by_css_selector("[ng-message='required']").is_displayed()
    pass