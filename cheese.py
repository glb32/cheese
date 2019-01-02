#cheese BOT 
#i want to die

import discord
from random import randint
import json
import time

token = ''
facts = ["There is no exact information regarding the origin of cheese, but archaeological studies have shown the origin of cheese dates as far back as 6000 BC. Studies also show that during that era, cheese was made from cow’s milk and goats in Mesopotamia.",
    "There are more than 2000 varieties of cheese available worldwide. Mozzarella is the favorite cheese around the globe, and the most consumed. It is used in pizza and many other recipes.",
    "People of Greece are the largest consumers of cheese worldwide. An average person from Greece consumes around 27.3 kg of cheese every year, about ¾ of which is feta cheese.",
    "Pizza Hut is the largest cheese-using fast food giant; it uses approximately 300 million pounds of cheese annually, mostly on pizza.",
    "Cheese production around the globe is more than the combined worldwide production of coffee, tobacco, tea, and cocoa beans.",
    "The first cheese factory was established in Switzerland in 1815; however, successful mass production began in 1851 in the United States.",
    "Contrary to popular belief, cheese, eaten in moderate quantities, is an excellent source of protein, calcium, and phosphorus. Its saturated fat content is responsible for its bad reputation. Even so, the benefits of eating cheese outweigh any negative effects.",
    "In the United States, the month of June is National Dairy Month and the last week of June is National Cheese Week.",
    "Cheese can be produced using a variety of milk including cow, buffalo, goat, horse, and even camel.",
    "A whopping 20 million metric tons of cheese is produced worldwide each year and production is increasing with growing demand.",
    "Approximately 10 pounds of milk is required to make one pound of cheese. If it wasn’t for cheese, a lot of milk would have been wasted.",
    "Cheese is kept for a period of time before it’s ready to eat. Some varieties of cheese, blue cheese, Gorgonzola, and brie are exposed to mold, which helps them age properly.",
    "During the Roman Empire, large Roman houses had separate kitchens for manufacturing cheese only, they were called careale.",
    "Some varieties of cheese like mozzarella, cheddar, Swiss and American, help prevent tooth decay. They promote the flow of saliva, which leads to elimination of sugar and acids from the mouth.",
    "Another benefit associated with cheese is that it helps protect tooth enamel and has an antibacterial effect. If consumed in moderate quantities it has various health benefits."
         ]
client = discord.Client()

@client.event
async def on_member_join(member):
    with open('users.json','r') as f:
        users = json.load(f)
    await client.send_message("{} CHEESE CHEESE".format(member.mention))
    await client.update_data(users,member)

    with open('users.json','w') as f:
        json.dump(users,f)
    f.close()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('cheese'):
        msg = 'CHEESE CHEESE CHEESE CHEESE CHEESE {0.author.mention}'.format(message)
        print("i smell cheese")

        await client.send_message(message.channel, msg)
        with open('users.json', 'r') as f:

            users = json.load(f)

        await update_data(users, message.author)
        await add_experience(users, message.author,5)
        await level_up(users,message.author,message.channel)
        with open('users.json', 'w') as f:
            json.dump(users,f)
        f.close()
    if message.content.startswith('?cheesefact'):

        await client.send_message(message.channel, facts[randint(0,14)])
    if message.content.startswith('?cheeseban'):
        await client.send_message(message.channel,'Alex the Wizard#0929 has been banned')


async def update_data(users,user):
    if not user.id in users:
         users[user.id] = {}
         users[user.id]['experience'] = 0
         users[user.id]['level'] = 0

async def add_experience(users,user,exp):
    users[user.id]['experience'] += exp

async def level_up(users,user,channel):
    experience = users[user.id]['experience']
    lvl_start = users[user.id]['level']
    lvl_end = int(experience ** 1/4)

    if lvl_start < lvl_end:
        await client.send_message(channel,'{} has cheesed it up to cheese level {}'.format(user.mention,lvl_end))
        users[user.id]['level'] += 1

@client.event
async def on_ready():
    print("CheeseBot v.1.0.2")
    print("starting...")
    time.sleep(1)
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
client.run(token)


