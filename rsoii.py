import discord
from discord.ext import commands
import asyncio
from itertools import cycle
import time
import datetime

TOKEN = 'NTE4NTUzMDU2NDg1MzEwNjMy.DuSdpw.jihEt-Ge5QXaU8LVKiLpHhzNg4c'

client = commands.Bot(command_prefix = '-')
status = ['Calling quorum...📝']
client.remove_command("help")


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
async def cmds():
    await client.say("**-cmds**: Display a list of commands.\n**-ping**: Check if the bot is responding quickly\n**-delete**: Deletes entered amount of messages. Must be more than 2 and less than 100 messages and the messages can not be over 2 weeks old. Format: `-delete <integer>`\n**-announce**: Make an announcement. Format: `-announce <text>`")
@client.command()
async def ping():
    await client.say('Pong!')

@client.command()
async def leaves():
    client.leave_server('518282234608877578')
    
@client.command(pass_context=True)
async def announce(ctx, *, message):
    if (ctx.message.author.id == ("147999751441219584") or ("67696910172950528") or ("201459061055684609")):
        server = client.get_server('467897785845284864')
        role = discord.utils.get(server.roles, name='Senator') 
        for member in server.members:
            if role in member.roles:
                embed = discord.Embed(
                timestamp = datetime.datetime.utcnow(),
                colour = discord.Colour.blue()
                )
                embed.set_footer(text='senate bot')
                embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/447514535373438976/522865617838145547/P1BmSBO3_400x400.jpg')
                embed.add_field(name='Announcement', value=message + '\n\nSent by: ' + ctx.message.author.mention, inline = False)
                await client.send_message(member, embed=embed)
    else:
        await client.say('You lack permission to use this command, if you have any questions or concerns please contact `snowbleed#7824`') 
            
@client.command(pass_context=True)
async def delete(ctx, amount=100):
    if (ctx.message.author.id in ["147999751441219584", "67696910172950528", "201459061055684609"]):
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
        
""" EMBED EXAMPLE
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
"""
client.loop.create_task(change_status())
client.run(TOKEN)
