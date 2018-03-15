print('  Everything Discord Bot 0.0.0 Canary')
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
from subprocess import Popen,STDOUT
from json import load
from shlex import split
from requests import get
print('i Imported required modules (discord,asyncio,subprocess,json.load,shlex.split,requests.get)')

tokenFileObj = open('../data/token.json','r')
tokenFileJsonRaw = load(tokenFileObj)
tokenFileObj.close()
tokenBot = tokenFileJsonRaw['token']
print('i Loaded ../variables/token.json')

client = discord.Client()
bot = commands.Bot(command_prefix = "?")
print('i client,bot inited')

@bot.event
async def on_ready():
    print('i Online & Connected')

@bot.event
async def on_message(message):
    # print('i Message Received ({})'.format(message.content))
    if message.content == 'evt:status':
        # print('i Message Responding (message[0:3] is {})'.format(message.content[0:3]))
        bot.send_message(message.channel,'Everything Discord Bot 0.0.0 Canary is doing fine.')
        # bot.send_message(message.channel, ':weary: Git Control is not finished...')
        # print('i Message Sent ({})'.format(':weary: Git Control is not finished...'))
    elif message.content.startswith('evt:ovw'):
        if message.content.startswith('evt:ovw:url'):
            getRq = get((message.content+' ')[12:-1])
            uiFileObj = open('../data/uiSub.py','w')
            bot.send_message(message.channel,'GET {} Response:\nStatus Code: {}\nText: {}'.format())
            uiFileObj.write(getRq.text)
            uiFileObj.close()
    elif message.content.startswith('evt:'):
        bot.send_message(message.channel,':warning: Everything is still in WIP...')
        process = Popen(['python3','../data/uiSub.py',message.content,tokenBot],stdout=-1,stderr=-1)
        stdout,stderr = process.comminucate()
        bot.send_message(message.channel,stdout)
