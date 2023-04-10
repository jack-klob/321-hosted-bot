import os
from dotenv import load_dotenv
import discord
from test_utils.testable_bot import TestableBot
import requests
import json

# backend currently must be hosted locally
baseurl = 'https://321-hosted-backend.jack-klob.repl.co'

load_dotenv()
TOKEN = os.environ['DISCORD_TOKEN']

bot = TestableBot(intents=discord.Intents.all(), command_prefix='!')

@bot.event
async def on_ready():
    print(f"{bot.user} has connected to the server")
    channel = bot.get_channel(1090771155163549796)
    await channel.send("Running")

@bot.event
async def on_message(message):
    print(message.content)
    await bot.process_commands(message)

@bot.command(name = 'create_task', help = 'Creates a task')
async def task_creation(ctx, *args):
    if not args:
        await ctx.send("No task name given")
        return

    title = " ".join(args)
    guild_id = ctx.guild.id

    url = baseurl + f"/task"
    response = requests.post(url=url, data={"title": title, 'guild' : guild_id})
    
    if response.status_code == 201:
        await ctx.send(f"The task \"{title}\" has been created!")
    else:
        await ctx.send("An error occured when trying to create the task")

def is_task_available(ctx, id):
    '''
    return true if the task exists and is available to the user
    return false if the tasks does not exist or is from another
    server
    '''
    task = json.loads(requests.get(url=f'{baseurl}/task/{id}').text)
    guild_id = ctx.guild.id

    if 'id' not in task or task['guild'] != guild_id:
        return False
    
    return True


@bot.command(name = 'delete_task', help = 'Deleted a task')
async def task_delete(ctx, id):
    url = f'{baseurl}/task/{id}'
    guild_id = ctx.guild.id

    if not is_task_available(ctx, id):
        await ctx.send(f'Task with id {id} does not exist')
        return
    
    r = requests.delete(url=url)
    print(r)
    
    if r.status_code == 204:
        await ctx.send(f'Task with id {id} deleted')
    else:
        await ctx.send("An error occured when trying to delete task")


@bot.command(name = 'due_date')
async def due_date(ctx, id, *args):
    due_date = " ".join(args)

    if not is_task_available(ctx, id):
        await ctx.send(f'Task with id {id} does not exist')
        return

    url = f'{baseurl}/due-date/{id}'
    data = {"due_date": due_date}
    response = requests.post(url=url, data=data)

    if response.status_code == 200:
        await ctx.send(f'Task {id} due date set to **{due_date}**')
    else:
        await ctx.send("Due date must be in format YYYY-MM-DD HH:MM")


def silence_mention(mention: str):
    if '&' in mention:
        return mention
    else:
        mention = mention[:2] + '&' + mention[2:]
        return mention


@bot.command(name = 'assign_user')
async def assign_user(ctx: discord.abc.Messageable, id = None, *args):
    if not id.isdigit():
        await ctx.send("Must provide id")
    url = f'{baseurl}/assignees/{id}'

    guild_id = ctx.guild.id

    if args is None:
        await ctx.send("No assignees given")
        return

    if not is_task_available(ctx, id):
        await ctx.send(f'Task with id {id} does not exist')
        return

    assignees = [*args]
    print(assignees)
    
    data = {"assignees": assignees}
    print(f"data: {data}")
    response = requests.put(url=url, data=data)

    no_mentions = discord.AllowedMentions.none()

    print(response)
    print(response.text)

    if response.status_code == 200:
        await ctx.send(f"assignees: {assignees} have been assigned to the task!", allowed_mentions=no_mentions)
    else:
        await ctx.send(f'{assignees} are already assigned to the task')
    
        

bot.run(TOKEN)