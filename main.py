import random

import discord
from discord.ext import commands

bot_token = "MTE2NTM1MjA0NDk5MTg4MTMzNw.GxqBqn.bwNxE3kQZwrrQuinMeD6nE0nb19XfXtfjRXPcc"

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

member = []
classes = ['아이언클래드', '사일런트', '디펙트', '와쳐']


@bot.event
async def on_ready():
  print(f'Logged in as {bot.user.name}')


@bot.event
async def on_message(message):
  if message.author == bot.user:
    return

  if message.content.startswith('!참가자'):
    global member
    temp_list = message.content[4:].split()
    if len(temp_list) != 4:
      await message.channel.send('인원이 총 4명이 아닙니다.')
      return
    member = temp_list
    await message.channel.send(f'참가 인원 {member}이 등록되었습니다.')

  if message.content.startswith('!뽑기'):
    random.shuffle(member)

    out_strings = []
    for _class, user in zip(classes, member, strict=False):
      out_strings.append(f'{_class}: {user}')

    await message.channel.send('\n'.join(out_strings))

  if message.content.startswith('!도움'):
    out_strings = [
        '**!참가자 <인원> <인원> <인원> <인원>** - 다함께 슬끼얏호우 참가자 설정', '**!뽑기** - 빛나는 뽑기!'
    ]
    await message.channel.send('\n'.join(out_strings))


bot.run(bot_token)
