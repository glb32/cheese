#cheese BOT 
#i want to die

import discord
from random import randint
import json
import time

token = ''
fopen = open("facts.txt")
def facts(index):
    fopen.readline(index)
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


