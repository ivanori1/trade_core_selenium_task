from behave import given, when, then, step


@step('Click Finish')
def step_impl(context):
    context.questionnaire.click_finish()
