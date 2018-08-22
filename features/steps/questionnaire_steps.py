from behave import given, when, then, step


@step('Click Finish')
def step_impl(context):
    context.questionnaire.click_finish()


@when('Select one of "{answer}" from Shares')
def step_impl(context, answer):
    context.questionnaire.select_from_shares(answer)


@then('One of the Shares dropdown "{answer}" will be visible')
def step_impl(context, answer):
    context.questionnaire.verify_answer_selected_from_shares(answer)


@when('Select one of "{answer}" from Forex')
def step_impl(context, answer):
    context.questionnaire.select_from_forex(answer)


@then('One of the Forex dropdown "{answer}" will be visible')
def step_impl(context, answer):
    context.questionnaire.verify_answer_selected_from_forex(answer)


@when('Select one of "{answer}" from CDFs')
def step_impl(context, answer):
    context.questionnaire.select_from_cdfs(answer)


@then('One of the CDFs dropdown "{answer}" will be visible')
def step_impl(context, answer):
    context.questionnaire.verify_answer_selected_from_cdfs(answer)


@when('Select "{platform}" from Trading Platform')
def step_impl(context, platform):
    context.questionnaire.select_from_relevant_trading_accounts(platform)


@then('Selected "{platform}" will be visible')
def step_impl(context, platform):
    context.questionnaire.verify_answer_selected_trading_accounts(platform)


@when('Select one of "{answer}" from Currency')
def step_impl(context, answer):
    context.questionnaire.select_currency(answer)


@then('One of the Currency dropdown "{answer}" will be visible')
def step_impl(context, answer):
    context.questionnaire.verify_answer_selected_currency(answer)


@when('Select one of "{answer}" from Income')
def step_impl(context, answer):
    context.questionnaire.select_annual_income(answer)


@then('One of the Income dropdown "{answer}" will be visible')
def step_impl(context, answer):
    context.questionnaire.verify_answer_selected_annual_income(answer)


@when('Select one of "{answer}" from Employment')
def step_impl(context, answer):
    context.questionnaire.select_employment_status(answer)


@then('One of the Employment dropdown "{answer}" will be visible')
def step_impl(context, answer):
    context.questionnaire.verify_answer_selected_employment_status(answer)


@when('Select one of "{answer}" from Savings')
def step_impl(context, answer):
    context.questionnaire.select_savings(answer)


@then('One of the Savings dropdown "{answer}" will be visible')
def step_impl(context, answer):
    context.questionnaire.verify_answer_selected_savings(answer)


@when('Check read terms')
def step_impl(context):
    context.questionnaire.check_read_terms()

@then('Portal account page will open')
def step_impl(context):
    assert context.questionnaire.verify_portal_page_is_open() == "https://demo-biq.dev.tradecore.io/#/portal/accounts"
