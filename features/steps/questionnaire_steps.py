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