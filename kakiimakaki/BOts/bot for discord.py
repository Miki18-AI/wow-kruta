from enum import member

import discord
import random
from aiohttp.helpers import TOKEN
from discord.permissions import permission_alias

intents = discord.Intents.all()
Perm = discord.Permissions.all()
Perm.ban_members = True
Perm.kick_members = True
intents.members = True
intents.message_content = True

TOKEN = 'MTM2NTAwODkzMzEyMjc0MDI2NA.G1DvpB.a8yoedzZTTBzPy44I4S_k5dnpwtM8_AVG6g2GM'
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents, permissions=Perm)
ANSWERS = {
    '!прив': 'Привет',
    'Как дела?': 'Было не очень, пока тебя не было',
    'Поиграем?': 'Да! Но я не знаю, во что ты играешь',
    'Ты классный': 'Спасибо! Ты тоже классный',
    'Пока': 'Прощай, мой друг',
}

GREETINGS = ['!прив','!здар','!здрав','!hi','!добр']

HOWAREYOU = {
    '!хорошо': 'Это хорошо, что хорошо',
    '!ок': 'Немногословно',
    '!плохо': 'Эх, хотел бы я помочь, но я всего лишь бот',
    '!так себе': 'Ну ничего, сейчас поиграешь с друзьями и твоё настроение улучшится',
    '!замечательно': 'У замечательных людей и дела замечательны',
    '!великолепно': 'Отлично, я рад за тебя!'
}
@client.event
async  def on_message(message):
    channel = message.channel
    for key in GREETINGS:
        if message.content.lower().startswith(key):
            await channel.send(ANSWERS['!прив'])

    def checkfunc (m):
        return m.content.lower() in HOWAREYOU and m.channel == channel

    if message.content.lower().startswith('!как дела?'):
        await channel.send('У меня всё хорошо, а у тебя?')
        msg = await client.wait_for('message', check=checkfunc)
        await channel.send(HOWAREYOU[msg.content.lower()])

    if message.content.lower().startswith('!забанить'):
        list = message.content.split()
        for member in client.get_all_members():
            if str(member) == str (list[1]):
                await channel.send(f"{member} был забанен {message.author}" )
                await member.ban(reason="Забанен, потому что потому", delete_message_days=1)

    if message.content.lower().startswith('!кикнуть'):
        list = message.content.split()
        for member in client.get_all_members():
            if str(member) == str (list[1]):
                await channel.send(f"{member} был выгнан {message.author}" )
                await member.kick(reason="Выгнан, потому что потому")
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
client.run(TOKEN)
