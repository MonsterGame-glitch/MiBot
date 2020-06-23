import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
from discord import Activity, ActivityType
import os

Bot = commands.Bot(command_prefix="*")

@Bot.command()
async def say(ctx,arg):
    await ctx.send(arg)

@Bot.command()
async def info(ctx,member:discord.Member):
    emb = discord.Embed(title='Информация о пользователе',color=0xffc600)
    emb.add_field(name="Когда присоединился:",value=member.joined_at,inline=False)
    emb.add_field(name='Айди:',value=member.id)
    emb.add_field(name="Аккаунт был создан:",value=member.created_at.strftime("%a,%#d %B %Y, %I:%M %p UTC"),inline=False)
    emb.add_field(name='Имя:',value=member.display_name,inline=False)
    emb.set_thumbnail(url=member.avatar_url)
    emb.set_footer(text=f"Вызвано:{ctx.message.author}",icon_url=ctx.message.author.avatar_url)
    emb.set_author(name=ctx.message.author,icon_url=ctx.message.author.avatar_url)
    await ctx.send(embed = emb)

@Bot.command()
@commands.has_permissions(view_audit_log=True)
async def mute(ctx,member:discord.Member,time:int,reason):
    channel = Bot.get_channel(724678191557509200)
    muterole = discord.utils.get(ctx.guild.roles,id=724636286580817991)
    emb = discord.Embed(title= "Мут",color=0xffc600)
    emb.add_field(name='Модератор',value=ctx.message.author.mention,inline=False)
    emb.add_field(name='Нарушитель',value=member.mention,inline=False)
    emb.add_field(name='Причина',value=reason,inline=False)
    emb.add_field(name="Время",value=time,inline=False)
    await member.add_roles(muterole)
    await channel.send(embed = emb)
    await asyncio.sleep(time * 60)
    await member.remove_roles(muterole)
@Bot.command()
@commands.has_permissions(view_audit_log=True)
async def unmute(ctx,member:discord.Member):
    channel = Bot.get_channel(724678191557509200)
    muterole = discord.utils.get(ctx.guild.roles,id=724636286580817991)
    emb = discord.Embed(title= "Анмут",color=0xff0000)
    emb.add_field(name='Модератор',value=ctx.message.author.mention,inline=False)
    emb.add_field(name='Нарушитель',value=member.mention,inline=False)
    await channel.send(embed = emb)
    await member.remove_roles(muterole)
@Bot.command()
@commands.has_permissions(view_audit_log=True)
async def kick(ctx,member:discord.Member,reason):
    channel = Bot.get_channel(724356255874809867)
    emb = discord.Embed(title= "Кик",color=0xffc600)
    emb.add_field(name='Модератор',value=ctx.message.author.mention,inline=False)
    emb.add_field(name='Нарушитель',value=member.mention,inline=False)
    emb.add_field(name='Причина',value=reason,inline=False)
    await member.kick()
    await channel.send(embed = emb)
@Bot.command()
@commands.has_permissions(view_audit_log=True)
async def ban(ctx,member:discord.Member,reason):
    channel = Bot.get_channel(724678191557509200)
    emb = discord.Embed(title= "Кик",color=0xffc600)
    emb.add_field(name='Модератор',value=ctx.message.author.mention,inline=False)
    emb.add_field(name='Нарушитель',value=member.mention,inline=False)
    emb.add_field(name='Причина',value=reason,inline=False)
    await member.ban()
    await channel.send(embed = emb)
@Bot.command()
@commands.has_permissions(view_audit_log=True)
async def clear(ctx,amount=1):
    clear = await ctx.message.channel.purge(limit=amount + 1)
@Bot.command()
@commands.has_permissions(view_audit_log=True)
async def clear_all(ctx,amount=9999):
    clear = await ctx.message.channel.purge(limit=amount)
@Bot.event
async def on_ready():
    print("Бот запустился")
    await Bot.change_presence(status=discord.Status.idle,activity=discord.Game("MiBot.io"))

token = os.environ.get('BOT_TOKEN')

bot.run(str(token))
