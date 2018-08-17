from behave import given, when, then


@given('Go to Tradecore')
def step_impl(context):
    context.browser.navigate("https://demo-biq.dev.tradecore.io/#/")
    assert context.browser.get_page_title() == "TradeCore - Step 1 | Registration"


@when('Click Next')
def step_impl(context):
    context.create_account.click_next()


@then('This field is required error')
def step_impl(context):
    assert context.create_account.verified_required_field_visible()


@when('Choose from Country dropdown')
def step_impl(context):
    context.create_account.select_country()


@then('Placeholder will change to selected country')
def step_impl(context):
    context.create_account.verified_country_is_selected()
