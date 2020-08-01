# sarthakeddy file
import discord
import requests
import json
import random

client = discord.Client()

@client.event
async def on_message(message):
    message.content = message.content.lower()
    if message.author == client.user:
        return
    channels = ["practice"]
    if str(message.channel) in channels:
        if message.content == 'help':
            embed = discord.Embed(title="Help BOT", description="Some useful commands")
            embed.add_field(name="hello", value="Greets the user")
            embed.add_field(name="!tags", value="Prints the different tags for questions")
            await message.channel.send(content=None, embed=embed)
        elif message.content == 'hello':
            await message.channel.send("Hello! Have you been practising")
        elif message.content.startswith("!tags"):
            prbl_tags = []
            mess = message.content
            start = 0
            i = 0
            for x in range(0, len(mess)):
                if " " == mess[i:i + 1][0]:
                    prbl_tags.append(mess[start:i + 1])
                    # print string[start:i+1]
                    start = i + 1
                i += 1
            prbl_tags.append(mess[start:i + 1])
            prbl_tags.pop(0)
            difficulty = int(prbl_tags[0])
            prbl_tags.pop(0)
            print(difficulty)
            link = "https://codeforces.com/api/problemset.problems?tags="
            for tag in prbl_tags:
                link += tag+";"
            request_link = requests.get(link)
            json_obj = json.loads(request_link.text)
            obj_result = json_obj['result']
            problems = obj_result['problems']
            problems_stat = obj_result['problemStatistics']
            i = 0
            flag = -1

            rnd_prblms = []
            for prb in problems:
                # print(prb[i]["name"])
                if problems[i]['rating'] >= difficulty:
                    flag = i
                    rnd_prblms.append(i)
                i += 1

            answer = ""
            if flag == -1:
                answer += "Sorry No problem exist for given tags.\nTry specifying individually."
            else :
                i = random.choice(rnd_prblms)
                print(problems[i]["name"])
                answer += "Problem Search Successful.\nName of problem: "
                answer += problems[i]['name'] + "\nLink to problem: "
                problem_link = "https://codeforces.com/problemset/problem/"
                problem_link += str(problems[i]['contestId']) + "/"
                problem_link += problems[i]['index']
                answer += problem_link
                answer += "\n"
                users = str(problems_stat[i]['solvedCount'])
                answer += users + " users solved this problem"
            await message.channel.send(answer)

# carl bot
client.run('NzM4NzE1NTc1NjMwNDMwMjY4.XyP8fQ.jtcCH_BJM-bxzUnyy5ztGFiiydo')