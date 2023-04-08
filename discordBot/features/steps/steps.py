import os
from dotenv import load_dotenv
from behave import *


@given('the secret')
def step_impl(context):
    load_dotenv()
    TOKEN = os.environ['TEST_TOKEN']


@when('the test bot tries to send a command')
def step_impl(context):
    pass


@then('the command is sent')
def step_impl(context):
    pass