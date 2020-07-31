import discord
from discord.ext import commands
import datetime


# https://discordapp.com/oauth2/authorize?client_id=738424005345804370&scope=bot&permissions=0
# id = 738424005345804370
def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()


token = read_token()
client = discord.Client()

@client.event
async def on_ready():
    print(f"{client.user} has connected to discord")


@client.event
async def on_member_join(member):
    mention=member.mention
    guild=member.guild
    await member.create_dm()
    await member.dm_channel.send(str(f"{mention}, Welcome to my server {guild}").format(mention=member,guild=guild))

    embed=discord.Embed(title=str("**New Member joined**"), colour=0x33c946, description=str(f"{mention} joined the {guild} :tulip: :cherries: :shaved_ice:").format(mention=member,guild=guild))
    embed.set_thumbnail(url=f"{member.avatar_url}")
    embed.set_author(name=f"{member.name}", icon_url=f"{member.avatar_url}")
    embed.set_footer(text=f"{member.guild}", icon_url=f"{member.guild.icon_url}")
    embed.timestamp=datetime.datetime.utcnow()
    embed.add_field(name="User ID:", value=member.id)
    embed.add_field(name="User Name :", value=member.display_name)
    embed.add_field(name="Server Name :", value=guild)
    embed.add_field(name="User Serial :", value=str(len(list(guild.members))))
    # Now get the channel where the message it to be posted by bot
    channel=discord.utils.get(member.guild.channels, id=int("738703325234462760"))
    await channel.send(embed=embed)


@client.event
async def on_message(message):
    id = client.get_guild(738424219821670470)
    if message.content.find("hello") != -1:
        await message.channel.send("Mai saurabh ka chatora bot")
    elif message.content.find("Bot sabse achha kaun hai?") != -1:
        await message.channel.send("Saurabh sir for sure")
    elif message.content.find("HELP ME WITH discord") != -1:
        await message.channel.send("https://www.youtube.com/watch?v=xdg39s4HSJQ")
    elif message.content == "users?":
        await message.channel.send(f"""Number of users ={id.member_count}""")


client.run(token)
