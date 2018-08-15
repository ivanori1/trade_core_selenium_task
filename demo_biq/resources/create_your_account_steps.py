from behave import given, when, then
from selenium import webdriver


driver = webdriver.Chrome


@given(u'Go to Tradecore')
def step_impl(context):
    driver.get("https://demo-biq.dev.tradecore.io/#/")


@when(u'Click Next')
def click_next():
    driver.find_element_by_id("button-step").click()


@then(u'This field is required error')
def verified_error_field_required():
    assert driver.find_element_by_css_selector("[ng-message='required']").is_displayed()
