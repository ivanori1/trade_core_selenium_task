from behave import given, when, then, step


@given('Go to Tradecore')
def step_impl(context):
    context.browser.navigate("https://demo-biq.dev.tradecore.io/#/")
    assert context.browser.get_page_title() == "TradeCore - Step 1 | Registration"


@step('Click Next')
def step_impl(context):
    context.create_account.click_next()


@then('Error appears: "{error_message}"')
def step_impl(context, error_message):
    assert context.create_account.verified_this_field__is_required_visible(error_message)


@when('Choose from country dropdown "{country}"')
def step_impl(context, country):
    context.create_account.select_country(country)


@then('Placeholder will change to selected country "{country}"')
def step_impl(context, country):
    context.create_account.verified_country_is_selected(country)

@when('Fill all placeholders')
def step_impl(context):
    context.create_account.type_first_name()
    context.create_account.type_last_name()
    context.create_account.type_email()
    context.create_account.type_password()
    context.create_account.type_phone()
    context.create_account.type_date_of_birth()
    context.create_account.type_postcode()
    context.create_account.type_address()
    context.create_account.type_city()

@when('Add invalid email credentials "{email}"')
def step_impl(context, email):
    context.create_account.type_email(email)
    context.create_account.type_email()