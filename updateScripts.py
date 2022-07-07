import discord

import requests
import json

from main import botColor
from main import bot

from replics import replic


async def on_guild_join(guild):
    text_channels = guild.text_channels
    if text_channels:
        channel = text_channels[0]

    embed = discord.Embed( title = 'Уютное местечко!', color = botColor)
    embed.description = replic['start']

async def инфо(ctx):
    if ctx.author != bot.user:
        embed = discord.Embed( title = 'О боте и его создателях:', color = botColor)
        embed.description = replic['info']
        embed.set_footer(text = f'Действие выполнено: {ctx.author.name}', icon_url = ctx.author.avatar_url)
        await ctx.send(embed = embed)


async def статус(ctx):
    if ctx.author != bot.user:
        embed = discord.Embed( title = 'Статус Бота:', color = botColor)
        embed.description = replic['status']
        embed.set_footer(text = f'Действие выполнено: {ctx.author.name}', icon_url = ctx.author.avatar_url)
        await ctx.send(embed = embed)


async def лис(ctx):
    response = requests.get('https://some-random-api.ml/img/fox') # Get-запрос
    json_data = json.loads(response.text) # Извлекаем JSON

    embed = discord.Embed(color = botColor, title = 'Случайно фото Лисички:') # Создание Embed'a
    embed.set_image(url = json_data['link']) # Устанавливаем картинку Embed'a
    await ctx.send(embed = embed) # Отправляем Embed


async def кот(ctx):
    response = requests.get('https://some-random-api.ml/img/cat') # Get-запрос
    json_data = json.loads(response.text) # Извлекаем JSON

    embed = discord.Embed(color = botColor, title = 'Случайно фото Котика:') # Создание Embed'a
    embed.set_image(url = json_data['link']) # Устанавливаем картинку Embed'a
    await ctx.send(embed = embed) # Отправляем Embed

async def помощь(ctx):
    embed = discord.Embed(color = botColor, title = 'Список возможных комманд бота:') # Создание Embed'a
    embed.description = replic['help']
    await ctx.send(embed = embed) # Отправляем Embed