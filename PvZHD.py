import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time

client = discord.Client()

messages = ["Hello Peashooter", "Hello Cherry Bomb", "Hello Chomper", "Hello Sunflower", "Hello Snow Pea", "Hello Potato Mine"]

@client.event
async def on_ready():
    print("Bot is online and connected to Discord")
    
    await client.change_presence(game=discord.Game(name='Making new videos with PvZHD! | kok'))

@client.event
async def on_message(message):
    if message.content.startswith("!info"):
       await client.send_message(message.channel, 'This server was made by PvZHD, go check his channel. and this is a basic bot.')
       
@client.event
async def on_member_join(member):
  channel = client.get_channel("439448762100875274")
  rules = client.get_channel("439798527607177226")
  msg = "Welcome! {} read the rules: {}".format(member.mention, rules.mention)
  await client.send_message(channel, msg)


@client.event
async def on_message(message):
    if message.content.startswith('!Greens'):
        await client.send_message(message.channel, 'https://cdn.discordapp.com/attachments/439448762100875274/440197911511302144/Z.png  Green Shadow!')

@client.event
async def on_message(message):
    if message.content.startswith('Hello'):
        await client.send_message(message.channel, 'Hi there.')

        
@client.event
async def on_member_remove(member):
   channel = client.get_channel("439448762100875274")
   msg = "Good-bye  {}".format(member.mention)
   await client.send_message(channel, msg)
   
@client.event
async def on_member_remove(member):
   channel = client.get_channel("439448762100875274")
   msg = "Good-bye  {}".format(member.mention)
   await client.send_message(channel, msg)                    
        

client.run("NDQwMTU2NjIyOTA4NTU1MjY0.DcdsZw.u6p3p5E2UReS5vxCfYy4TdIxoVQ")
