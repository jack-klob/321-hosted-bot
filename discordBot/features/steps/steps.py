from behave import *

@given(u'a user')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given a user')


@when(u'the user inputs a command to create a task')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the user inputs a command to create a task')


@then(u'the bot responds with a confimation message of the task creation')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the bot responds with a confimation message of the task creation')