# SELTFOX (c) 2022, All rights reserved.
# Nikatsu bot, kernel file.
# 
#
# DO NOT USE THE CODE IN COMMERCIAL PROJECTS.
# Owner: seltfox#2356.

import discord
from discord.ext import commands

import requests
import json
import asyncio

from configs import config
from replics import replic

import updateScripts

botColor = 0x503f59 # dark purple

bot = commands.Bot(command_prefix=config['prefix'])

if __name__ == "__main__":

    @bot.event
    async def on_ready():
        await bot.change_presence( status = discord.Status.online, activity = discord.Game("https://nikatsubot.github.io"))

    #@bot.command()
    #@commands.has_permissions(administrator=True)
    #async def создатьмр(ctx):
    #    global ROLE_MUTED
    #    guild = ctx.guild
    #    perms = discord.Permissions(2048) # send messages
    #    mrole = await guild.create_role(name="Мьют (NB)")
    #    await mrole.edit(permissions=perms)
    #    ROLE_MUTED = mrole.id
    #    await ctx.send(f"Роль мьюта бота успешно создана. ID: {ROLE_MUTED}")

    @bot.command()
    @commands.has_permissions(administrator=True) # timeout_members from ds
    async def мьют(ctx, user: discord.Member, time: int,*, reason="Причина не указана"):
        global ROLE_MUTED
        ROLE_MUTED = discord.utils.get(ctx.message.guild.roles, name="NBMUTE")

        role = user.guild.get_role(ROLE_MUTED) # айди роли мьюта которую будет получать юзер

        embed = discord.Embed( title = 'Участник был замьючен!', color = botColor)
        embed.description = f'''Участнику {user} выдали мьют!\nПродолжительность: {time} минут(-а).\nПричина выдачи: {reason}.'''
        embed.set_footer(text = f'Действие выполнено: {ctx.author.name}', icon_url = ctx.author.avatar_url)
        await ctx.send(embed = embed)
        await user.add_roles(role) #выдает мьют роль
        await asyncio.sleep(time * 60) #ждет нужное кол-во секунд умноженных на 60(вы выдаете мут на минуты. Допустим time = 10, то вы выдали мут на 10 минут)
        await user.remove_roles(role) #снимает мьют роль

    @bot.command()
    @commands.has_permissions(administrator=True)
    async def размьют(ctx, user: discord.Member):
        global ROLE_MUTED
        ROLE_MUTED = discord.utils.get(ctx.message.guild.roles, name="NBMUTE")

        role = user.guild.get_role(ROLE_MUTED) # айди роли мьюта которую будет получать юзер

        embed = discord.Embed( title = 'Участник был размьючен!', color = botColor)
        embed.description = f"""Участнику {user} сняли мьют!"""
        embed.set_footer(text = f'Действие выполнено: {ctx.author.name}', icon_url = ctx.author.avatar_url)
        await ctx.send(embed = embed)
        await user.remove_roles(role) #снимает мьют роль

    @bot.command()
    @commands.has_permissions(administrator=True)
    async def кик(ctx, user : discord.User(), *arg, reason='Причина не указана'):
        await bot.kick(user)

        embed = discord.Embed( title = 'Участник был кикнут!', color = botColor)
        embed.description = f"""Участника {user} изгнали с сервера!"""
        embed.set_footer(text = f'Действие выполнено: {ctx.author.name}', icon_url = ctx.author.avatar_url)
        await ctx.send(embed = embed)

    @bot.event
    async def on_guild_join(guild):
        await updateScripts.on_guild_join(guild)

    @bot.command()
    async def инфо(ctx):
        await updateScripts.инфо(ctx)

    @bot.command()
    async def статус(ctx):
        if ctx.author != bot.user:
            embed = discord.Embed( title = 'Статус Бота:', color = botColor)
            embed.description = f"Статус: `Бот в рабочем состоянии.`\nКоличество серверов где есть я: {str(len(bot.guilds))}"
            embed.set_footer(text = f'Действие выполнено: {ctx.author.name}', icon_url = ctx.author.avatar_url)
            await ctx.send(embed = embed)

    @bot.command()
    async def лис(ctx):
        await updateScripts.лис(ctx)

    @bot.command()
    async def кот(ctx):
        await updateScripts.кот(ctx)

    @bot.command()
    async def помощь(ctx):
        await updateScripts.помощь(ctx)

    bot.run(config['token'])