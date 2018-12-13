import discord
from discord.ext import commands
import asyncio
from itertools import cycle
import time

TOKEN = 'NTE4NTUzMDU2NDg1MzEwNjMy.DuSdpw.jihEt-Ge5QXaU8LVKiLpHhzNg4c'

client = commands.Bot(command_prefix = '-')
status = ['Calling quorum...📝']
needsConfirmation = False
announcementConfirm = False

async def change_status():
    await client.wait_until_ready()
    msgs = cycle(status)

    while not client.is_closed:
        current_status = next(msgs)
        await client.change_presence(game=discord.Game(name=current_status))
        await asyncio.sleep(5)

@client.event
async def on_ready():
    print("Bot is online")

@client.command()
async def displayembed():
    embed = discord.Embed(
        title = 'Title',
        description = 'This is a description',
        colour = discord.Colour.blue()
    )

    embed.set_footer(text='This is a footer')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/518210617744818206/518463077541216258/kava.jpg')
    embed.set_author(name='Snowbleed')
    icon_url='https://cdn.discordapp.com/attachments/518210617744818206/518463077541216258/kava.jpg'
    embed.add_field(name='Snowbleed', value='Field Value', inline = False)
    embed.add_field(name='Snowbleed', value='Field Value', inline = True)
    embed.add_field(name='Snowbleed', value='Field Value', inline = True)

    await client.say(embed=embed)

@client.command()
async def cmds():
    await client.say("**-cmds**: Display a list of commands.\n**-ping**: Check if the bot is responding quickly\n**-delete**: Deletes entered amount of messages. Must be more than 2 and less than 100 messages and the messages can not be over 2 weeks old. Format: `-delete <integer>`\n**-announce**: Make an announcement. Format: `-announce <text>`")
@client.command()
async def ping():
    await client.say('Pong!')

@client.command(pass_context=True)
async def announce(ctx, *args):
    if {'Commanding Officer', 'Executive Officer', 'Sentry In Charge'} & {role.name for role in ctx.message.author.roles}:
        output = ''
        for word in args:
            output += word
            output += ' '
        announcementConfirm = True
        if announcementConfirm == True:
            await client.say('You are about to make an announcement, if you are sure please say -confirm')
            msg = await client.wait_for_message(author=ctx.message.author, content='-confirm')
            await client.send_message(client.get_channel('518286982145900575'), "@everyone " + output)
            announcementConfirm = False
    else:
        await client.say('You lack permission to use this command')
@client.command(pass_context=True)
async def training(ctx, arg1, arg2):
    author = ctx.message.author.mention
    if {'Commanding Officer', 'Executive Officer', 'Sentry In Charge'} & {role.name for role in ctx.message.author.roles}:
        if arg1 == 'mandatory':
            output = '@everyone MANDATORY TRAINING AT https://www.roblox.com/games/' + arg2 + '/-- HOSTED BY ' + author
            channel = '518286982145900575'
            needsConfirmation = True
        elif arg1 == 'optional':
            output = '@everyone OPTIONAL TRAINING AT https://www.roblox.com/games/' + arg2 + '/-- HOSTED BY ' + author
            channel = '518286982145900575'
            needsConfirmation = True
        else:
            output = 'Incorrect formatting: `-training <mandatory/optional> <placeid>`'
            channel = str(ctx.message.channel.id)
            needsConfirmation = False
        if needsConfirmation == True:
            await client.say('You are about to announce a training, if you are sure please say -confirm')
            msg = await client.wait_for_message(author=ctx.message.author, content='-confirm')
            await client.send_message(client.get_channel(channel), output)
            await client.say("Training announced.")
            needsConfirmation = False
        else:
            await client.say(output)
    else:
        await client.say('You lack permission to use this command')

@client.command(pass_context=True)
async def delete(ctx, amount=100):
    if {'Commanding Officer', 'Executive Officer', 'Sentry In Charge'} & {role.name for role in ctx.message.author.roles}:
        if ((amount > 1) and (amount < 100)):
            channel = ctx.message.channel
            messages = []
            async for message in client.logs_from(channel, limit=int(amount) + 1):
                messages.append(message)
            await client.delete_messages(messages)
            message = await client.say(str(amount) + " messages were deleted")
            await asyncio.sleep(5)
            await client.delete_message(message)
        else:
            message = await client.say('Incorrect formatting: `-delete <integer>`. Note however that you can not delete less than 2 or more than 100 messages nor can the messages be over 2 weeks old.')
            await asyncio.sleep(5)
            await client.delete_message(message)
    else:
        await client.say("You lack permission to use this command")

@client.command(pass_context=True)
async def logout(ctx):
    if ctx.message.author.id == "147999751441219584":
        await client.logout()
    else:
        await client.say('You lack permission to use this command')

client.loop.create_task(change_status())
client.run(TOKEN)
