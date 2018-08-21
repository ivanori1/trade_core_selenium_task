from features.base.browser import Browser
from features.pages.create_account_page import CreateAccount
from features.pages.questionnaire_page import Questionnaire


def before_all(context):
    context.browser = Browser()
    context.create_account = CreateAccount()
    context.questionnaire = Questionnaire()


def after_all(context):
    context.browser.close()
