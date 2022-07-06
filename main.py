import discord
from discord.ext import commands

import requests
import json
import asyncio

from configs import config

botColor = 0x503f59 # dark purple

bot = commands.Bot(command_prefix=config['prefix'])

@bot.event
async def on_ready():
         await bot.change_presence( status = discord.Status.online, activity = discord.Game("https://minikaitsu.github.io"))

@bot.command()
async def инфо(ctx):
    if ctx.author != bot.user:
        embed = discord.Embed( title = 'О боте и его создателях:', color = botColor)
        embed.description = f"""Я — Мифическая девятихвостая Лисица по имени Миникайцу, из рода Кицунэ родом из Японии. По фольклёру мы обладаем большими знаниями о мире и очень милы!
        Но всё же, я тут — чтобы помогать вам следить за порядком на сервере! Меня необязательно настраивать, не переживайте, просто расслабьтесь и занимайтесь своими делами.
        Для ознакомления с ботом воспользуйтесь функцией `?помощь`.
        Если же у вас возникли проблемы с ботом, вы можете обратиться с проблемой написав в лс seltfox#2356 или на наш сервер(Ссылка в профиле бота).
        SeltFox (c)2022, версия бота v.1.1 - дата: 06.07.2022. (Не является коммерческим проектом и никак не монитизируется!)"""
        embed.set_footer(text = f'Действие выполнено: {ctx.author.name}', icon_url = ctx.author.avatar_url)
        await ctx.send(embed = embed)

@bot.command()
async def статус(ctx):
    if ctx.author != bot.user:
        embed = discord.Embed( title = 'Статус Бота:', color = botColor)
        embed.description = f"""Статус бота: `Включен, иногда перезапускается на долю секунду, так как он все ещё в разработке`.
                                        Бот часто выключается с 0:30 до 10:00 по Астанинскому времени (МСК+3, UTC+6)
                                        Просим прощения за частое отключение бота, просто мы физически не можем оставлять его включеным.
                                        В данный момент мы активно ищем хостинг на который можно будет перевести бота для того, чтобы он радовал вас 24/7.
                                        Если вы готовы нам помочь, можете написать в лс seltfox#2356 или на наш сервер(Ссылка в профиле бота), будем рады любой помощи!
                                        ~ С любовью, seltfox и служба поддержки бота."""
        embed.set_footer(text = f'Действие выполнено: {ctx.author.name}', icon_url = ctx.author.avatar_url)
        await ctx.send(embed = embed)

@bot.command()
async def лис(ctx):
    response = requests.get('https://some-random-api.ml/img/fox') # Get-запрос
    json_data = json.loads(response.text) # Извлекаем JSON

    embed = discord.Embed(color = botColor, title = 'Случайно фото Лисички:') # Создание Embed'a
    embed.set_image(url = json_data['link']) # Устанавливаем картинку Embed'a
    await ctx.send(embed = embed) # Отправляем Embed

@bot.command()
async def кот(ctx):
    response = requests.get('https://some-random-api.ml/img/cat') # Get-запрос
    json_data = json.loads(response.text) # Извлекаем JSON

    embed = discord.Embed(color = botColor, title = 'Случайно фото Котика:') # Создание Embed'a
    embed.set_image(url = json_data['link']) # Устанавливаем картинку Embed'a
    await ctx.send(embed = embed) # Отправляем Embed

@bot.command()
@commands.has_any_role(979669031319646238) # id ролей
async def мьют(ctx, user: discord.Member, time: int,*, reason="Причина не указана"):
    role = user.guild.get_role(988303441543696395) # айди роли мьюта которую будет получать юзер

    embed = discord.Embed( title = 'Участник был замьючен!', color = botColor)
    embed.description = f"""Участнику {user} выдали мьют!
                            Продолжительность: {time} минут(-а).
                            Причина выдачи: {reason}!"""
    embed.set_footer(text = f'Действие выполнено: {ctx.author.name}', icon_url = ctx.author.avatar_url)
    await ctx.send(embed = embed)
    await user.add_roles(role) #выдает мьют роль
    await asyncio.sleep(time * 60) #ждет нужное кол-во секунд умноженных на 60(вы выдаете мут на минуты. Допустим time = 10, то вы выдали мут на 10 минут)
    await user.remove_roles(role) #снимает мьют роль

@bot.command()
@commands.has_any_role(979669031319646238)
async def размьют(ctx, user: discord.Member):
    role = user.guild.get_role(988303441543696395) # айди роли мьюта которую будет получать юзер

    embed = discord.Embed( title = 'Участник был размьючен!', color = botColor)
    embed.description = f"""Участнику {user} сняли мьют!"""
    embed.set_footer(text = f'Действие выполнено: {ctx.author.name}', icon_url = ctx.author.avatar_url)
    await ctx.send(embed = embed)
    await user.remove_roles(role) #снимает мьют роль


@bot.command()
async def помощь(ctx):
    embed = discord.Embed(color = botColor, title = 'Список возможных комманд бота:') # Создание Embed'a
    embed.description = """**Внимание, команды для модерации будут доступны только при наличии прав модерации у вас.**
                           `помощь` - Вызов этого списка.
                           `инфо` - Информация о боте.
                           `статус` - Статус бота. Здесь же иногда могут появляться заметки автора.
                           `мьют {участник} {время}` - Мьютит участника на n-ое количество минут.
                           `размьют {участник}` - Снимает мьют с участника.

                           `лис` - Отправляет случайное фото лисы/лиса. <3
                           `кот` - Отправляет случайное фото кота/кошки. ^-^"""
    await ctx.send(embed = embed) # Отправляем Embed

#@bot.command()
#async def мьют(ctx):
#    await member.edit(mute = True)

bot.run(config['token'])