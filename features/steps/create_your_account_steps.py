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
    context.create_account.verified_this_field__is_required_visible(
        error_message) or context.create_account.verified_other_error_message(error_message)


@when('Choose from country dropdown "{country}"')
def step_impl(context, country):
    context.create_account.select_country(country)


@then('Placeholder will change to selected country "{country}"')
def step_impl(context, country):
    context.create_account.verified_country_is_selected(country)


@step('Fill all placeholders')
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


@when('Add invalid password credentials "{password}"')
def step_impl(context, password):
    context.create_account.type_password(password)


@when('Type number "{tel_num}" to phone')
def step_impl(context, tel_num):
    context.create_account.type_phone(tel_num)


@then('Selected flag is "{country}')
def step_impl(context, country):
    context.create_account.verified_selected_flag(country)
