from behave import given, when, then
from selenium.webdriver.common.by import By


@given('Go to Tradecore')
def step_impl(context):
    context.create_account.navigate("https://demo-biq.dev.tradecore.io/#/")
    assert context.create_account.get_page_title() == "TradeCore - Step 1 | Registration"

@when('Click Next')
def step_impl(context):
    context.driver.find_element(By.ID, "button-step").click()


@then('This field is required error')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, "[ng-message='required']").is_displayed()