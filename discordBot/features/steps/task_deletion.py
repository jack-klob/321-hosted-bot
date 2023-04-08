import os
from behave import *
from dotenv import load_dotenv
from test_utils.test_bot_commands import TestBotCommands
from test_utils.api_connection import APIConnection
from hamcrest import assert_that, equal_to
import json



@given(u'a task "{task_name}" has been created')
def step_impl(context,task_name):
    APIConnection.create_task(task_name)

    
@when(u'the user inputs "!delete_task <id>" with the id of the task')
def step_impl(context):
    tasks = json.loads(APIConnection.get_list().text)
    context.id = tasks[-1]['id']

    context.commands.send_message(f'!delete_task {context.id}')
    


@then(u'the bot outputs "Task with id <id> deleted"')
def step_impl(context):
    reply = context.commands.read_reply()['content']
    expected = f'Task with id {context.id} deleted'
    assert_that(reply, equal_to(expected))


@then(u'the task with that id is deleted')
def step_impl(context):
    response = APIConnection.get_task(context.id)
    assert_that(response.status_code, equal_to(404))
