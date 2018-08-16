from features.base.browser import Browser
from features.pages.create_account_page import CreateAccount


def before_all(context):
    context.browser = Browser()
    context.create_account = CreateAccount()


def after_all(context):
    context.browser.close()
