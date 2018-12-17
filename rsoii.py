import discord
from discord.ext import commands
import asyncio
from itertools import cycle
import time
import datetime

TOKEN = 'NTE4NTUzMDU2NDg1MzEwNjMy.DuSdpw.jihEt-Ge5QXaU8LVKiLpHhzNg4c'

client = commands.Bot(command_prefix = '-')
status = ['Calling quorum...📝']
authorizedusers = ["147999751441219584", "67696910172950528", "201459061055684609"]
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
@client.command(pass_context=True)
async def grr(ctx):
    if (ctx.message.author.id in ["147999751441219584", "239846207634014210", "172128816280371200"]):
        await client.send_message(ctx.message.author, "What the fuck did you just fucking say about me, you little bitch? I’ll have you know I graduated top of my class in the Marine Security Guard Battalion, and I’ve been involved in numerous secret raids on Al-Quaeda, and I have over 300 confirmed kills. I am trained in gorilla warfare and I’m the top sniper in the entire US armed forces. You are nothing to me but just another target. I will wipe you the fuck out with precision the likes of which has never been seen before on this Earth, mark my fucking words. You think you can get away with saying that shit to me over the Internet? Think again, fucker. As we speak I am contacting my secret network of spies across the USA and your IP is being traced right now so you better prepare for the storm, maggot. The storm that wipes out the pathetic little thing you call your life. You’re fucking dead, kid. I can be anywhere, anytime, and I can kill you in over seven hundred ways, and that’s just with my bare hands. Not only am I extensively trained in unarmed combat, but I have access to the entire arsenal of the United States Marine Corps and I will use it to its full extent to wipe your miserable ass off the face of the continent, you little shit. If only you could have known what unholy retribution your little “clever” comment was about to bring down upon you, maybe you would have held your fucking tongue. But you couldn’t, you didn’t, and now you’re paying the price, you goddamn idiot. I will shit fury all over you and you will drown in it. You’re fucking dead, kiddo.")
    else:
         await client.send_message(ctx.message.author, "sorry bud, this command aint for u.")
@client.command()
async def leaves():
    server = client.get_server('518282234608877578')
    await client.leave_server(server)
    
    
@client.command(pass_context=True)
async def bill(ctx):
    server = client.get_server('467897785845284864')
    member = server.get_member(ctx.message.author.id)
    role = discord.utils.get(server.roles, name='Senator') 
    role1 = discord.utils.get(server.roles, name='Senate Minority Leader')
    role2 = discord.utils.get(server.roles, name='Senate Majority Leader')
    role3 = discord.utils.get(server.roles, name='Secretary of the Senate')
    role4 = discord.utils.get(server.roles, name='Acting PPT')
    role5 = discord.utils.get(server.roles, name='President Pro-Tempore')
    role6 = discord.utils.get(server.roles, name='President of the Senate') 
    rolelist = [role, role1, role2, role3, role4, role5, role6,]
    gotrole = any(elem in rolelist for elem in server.member.roles)
    if gotrole:
        await client.say("you are a senator, congrats")
        
@client.command(pass_context=True)
async def announce(ctx, *, message):
    global authorizedusers
    if (ctx.message.author.id in authorizedusers):
        server = client.get_server('467897785845284864')
        role = discord.utils.get(server.roles, name='Senator') 
        role1 = discord.utils.get(server.roles, name='Senate Minority Leader')
        role2 = discord.utils.get(server.roles, name='Senate Majority Leader')
        role3 = discord.utils.get(server.roles, name='Secretary of the Senate')
        role4 = discord.utils.get(server.roles, name='Acting PPT')
        role5 = discord.utils.get(server.roles, name='President Pro-Tempore')
        role6 = discord.utils.get(server.roles, name='President of the Senate')
        await client.say('You are about to make an announcement, if you are sure please say -confirm')
        msg = await client.wait_for_message(author=ctx.message.author)
        if msg.content == '-confirm':
            for member in server.members:
                if {role, role1, role2, role3, role4, role5, role6}.union(member.roles):
                    embed = discord.Embed(
                    timestamp = datetime.datetime.utcnow(),
                    colour = discord.Colour.blue()
                    )
                    embed.set_footer(text='senate bot')
                    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/447514535373438976/522865617838145547/P1BmSBO3_400x400.jpg')
                    embed.add_field(name='Announcement', value=message + '\n\nSent by: ' + ctx.message.author.mention, inline = False)
                    await client.send_message(member, embed=embed)
        else:
            await client.say("Announcement not sent")
            return
    else:
        await client.say('You lack permission to use this command, if you have any questions or concerns please contact `snowbleed#7824`') 
            
@client.command(pass_context=True)
async def delete(ctx, amount=100):
    global authorizedusers
    if (ctx.message.author.id in authorizedusers):
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
