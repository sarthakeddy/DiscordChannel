import discord
# id = 738424005345804370
def read_token():
    with open("token.txt", "r") as f:
        lines=f.readlines()
        return lines[0].strip()

token = read_token()
client=discord.Client()

@client.event
async def on_member_join(member):
        for channel in member.server.channels:
                if str(channel) == "general":
                        await  client.send_message(f"""Welcome to server {member.mention}""")


@client.event
async def on_message(message):
        id = client.get_guild(738424005345804370)
        if message.content.find("hello")!=-1:
            await message.channel.send("Hi")
        elif message.content =="users?":
            await message.channel.send(f"""Number of users ={id.member_count}""")
client.run(token)