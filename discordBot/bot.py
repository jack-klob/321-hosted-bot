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

@bot.command(name = 'delete_task', help = 'Deleted a task')
async def task_delete(ctx, id):
    url = f'{baseurl}/task/{id}'
    guild_id = ctx.guild.id

    task = json.loads(requests.get(url=url).text)

    if 'id' not in task or task['guild'] != guild_id:
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
    url = f'{baseurl}/task/{id}'
    due_date = " ".join(args)
    guild_id = ctx.guild.id
    task = json.loads(requests.get(url=url).text)

    if 'id' not in task or task['guild'] != guild_id:
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
async def assign_user(ctx: discord.abc.Messageable, id, *args):

    url = f'{baseurl}/assignees/{id}'

    if args is None:
        await ctx.send("No assignees given")
        return

    assignees = [*args]
    user_ids = [username[2:-1] for username in assignees]
    print(user_ids)
    print(assignees)
    
    data = {"assignees": user_ids}
    print(f"data: {data}")
    response = requests.put(url=url, data=data)

    no_mentions = discord.AllowedMentions.none()

    print(response)

    if response.status_code == 200:
        await ctx.send(f"assignees: {assignees} have been assigned to the task!", allowed_mentions=no_mentions)
    else:
        await ctx.send("A problem occurred when trying to add a assignees")
    
        

bot.run(TOKEN)