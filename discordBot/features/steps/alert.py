
from behave import *
from dotenv import load_dotenv
from test_utils.test_bot_commands import TestBotCommands
from test_utils.api_connection import APIConnection
from hamcrest import assert_that, equal_to

@when(u'the user inputs <!add_alert <id>  "2023-04-09 11:55"> with the id of a task')
def step_impl(context):
   context.commands.send_message(f'!add_alert {context.id} 2023-04-09 11:55')


@then(u'the bot outputs "Alert has been assigned to the task!"')
def step_impl(context):
    reply = context.commands.read_reply()['content']
    expected = f'Alert has been assigned to the task!'
    assert_that(reply, equal_to(expected))


@given(u'the task with id <id> has an alert time of "2023-04-09 11:55" added')
def step_impl(context):
    context.commands.send_message(f'!add_alert {context.id} 2023-04-09 11:55')


@when(u'the alert time has been passed or matches the current time')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the alert time has been passed or matches the current time')

@when(u'I wait \'60\' seconds')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I wait \'60\' seconds')


@then(u'the bot outputs "@everyone An alert for a task with id: <id> has occured!"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the bot outputs "@everyone An alert for a task with id: <id> has occured!"')