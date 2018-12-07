import discord
from discord.ext import commands
import asyncio
from itertools import cycle
import time

TOKEN = 'NTE4NTUzMDU2NDg1MzEwNjMy.DuSdpw.jihEt-Ge5QXaU8LVKiLpHhzNg4c'

client = commands.Bot(command_prefix = '-')
status = ['Merry Christmas, Marines!']
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
    await client.say("**-cmds**: Display a list of commands.\n**-ping**: Check if the bot is responding quickly\n**-delete**: Deletes entered amount of messages. Must be more than 2 and less than 100 messages and the messages can not be over 2 weeks old. Format: `-delete <integer>`\n**-announce**: Make an announcement. Format: `-announce <text>`\n**-training**: Announce a training. Format: `-training <mandatory/optional> <placeid>`\n**-deploy**: Announce a sentry deployment. Format: `-deploy <placeid>`")

@client.command()
async def ping():
    await client.say('Pong!')

@client.command()
async def grr():
    await client.say("What the fuck did you just fucking say about me, you little bitch? I’ll have you know I graduated top of my class in the Marine Security Guard Battalion, and I’ve been involved in numerous secret raids on Al-Quaeda, and I have over 300 confirmed kills. I am trained in gorilla warfare and I’m the top sniper in the entire US armed forces. You are nothing to me but just another target. I will wipe you the fuck out with precision the likes of which has never been seen before on this Earth, mark my fucking words. You think you can get away with saying that shit to me over the Internet? Think again, fucker. As we speak I am contacting my secret network of spies across the USA and your IP is being traced right now so you better prepare for the storm, maggot. The storm that wipes out the pathetic little thing you call your life. You’re fucking dead, kid. I can be anywhere, anytime, and I can kill you in over seven hundred ways, and that’s just with my bare hands. Not only am I extensively trained in unarmed combat, but I have access to the entire arsenal of the United States Marine Corps and I will use it to its full extent to wipe your miserable ass off the face of the continent, you little shit. If only you could have known what unholy retribution your little “clever” comment was about to bring down upon you, maybe you would have held your fucking tongue. But you couldn’t, you didn’t, and now you’re paying the price, you goddamn idiot. I will shit fury all over you and you will drown in it. You’re fucking dead, kiddo.")
    
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

@client.command()
async def snow():
    await client.say("bleed")

@client.command()
async def frost():
    await client.say("bleed")

@client.command(pass_context=True)
async def deploy(ctx, arg1):
    if {'Commanding Officer', 'Executive Officer', 'Sentry In Charge'} & {role.name for role in ctx.message.author.roles}:
        output = "**NOTICE:** A sentry/protection deployment order has been issued. All sentries are ordered to respond to https://www.roblox.com/games/" + arg1 + "/--  immediately.  @everyone"
        await client.say('You are about to announce a deployment, if you are sure please say -confirm')
        msg = await client.wait_for_message(author=ctx.message.author, content='-confirm')
        await client.send_message(client.get_channel('518286886251397121'), output)
        await client.say("Deployment announced.")
        needsConfirmation = False
    else:
        await client.say("You lack permission to use this command")

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
