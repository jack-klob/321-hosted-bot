import os
from behave import *
from dotenv import load_dotenv
from test_bot import TestBotCommands
from hamcrest import assert_that, equal_to

@given(u'a user')
def step_impl(context):
    load_dotenv()
    TOKEN = os.environ['TEST_TOKEN']
    context.commands = TestBotCommands(TOKEN)


@when(u'the user inputs a command to create a task')
def step_impl(context):
    context.commands.send_message("!create_task new task")


@then(u'the bot responds with a confimation message of the task creation')
def step_impl(context):
    message = context.commands.read_reply()['content']
    assert_that(message, equal_to("The task \"new task\" has been created!"))