import time 
from behave import *
from dotenv import load_dotenv
from test_utils.test_bot_commands import TestBotCommands
from test_utils.api_connection import APIConnection
from hamcrest import assert_that, equal_to
from datetime import datetime

@then(u'the bot outputs "id: <id>, Created task from test, [], None, None"')
def step_impl(context):
    reply = context.commands.read_reply()['content']
    expected = f'id: {context.id}, Created task from test, [], None, None'
    assert_that(reply, equal_to(expected))


@given(u'a user testUser has been assigned to the task with id <id>')
def step_impl(context):
    context.commands.send_message(f'!assign_user {context.id} testUser')
    time.sleep(1)


@then(u'the bot outputs "id: <id>, Created task from test, [\'testUser\'], None, None"')
def step_impl(context):
    reply = context.commands.read_reply()['content']
    expected = f'id: {context.id}, Created task from test, [\'testUser\'], None, None'
    assert_that(reply, equal_to(expected))