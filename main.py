from email import message
import time
import disnake
from disnake import FFmpegPCMAudio
from disnake.ext import commands 
from disnake.utils import get
import random

token = 'bot_token'


bot = commands.InteractionBot()

        

@bot.event
async def on_ready():
        print("working)")
        await bot.change_presence(activity=disnake.Activity(type=disnake.ActivityType.listening, name="zitraks mode"))

@bot.event
async def on_member_join(member):
        role = member.guild.get_role(role_id)
        await member.add_roles(role)

@bot.event
async def on_message(message):
        author = message.author
        guild_id = str(message.guild.id)

        if author.bot:
            return

        if message.channel.id == (channel_id):
            await message.add_reaction('👍🏻')
            await message.add_reaction('👎🏻')

@bot.slash_command(name = "clear",
                   description= "очистка чата",
                   dm_permission= True
                  )
async def clear(interaction: disnake.CommandInteraction):
        await interaction.channel.purge(limit = 5)

@bot.slash_command(name = "help")
async def help(ctx):
        emb = ("""> Выдаёт роль новым участникам\n\n> Ставит реакции в канале <#1027185837869371422>\n\n||Разраб: NANON#0222||""")
        embed = disnake.Embed(title = "Возможности бота:",
        description= "Префикс -  .\n\n.avatar - Показывает аватарку участника\n\n.stats - Статистика сервера\n\n.admin - Выдаёт админку\n\n.love - Сами разберётесь\n\n",
        color = disnake.Color.from_rgb(255,250,250)
        )
        embed.add_field(name = "Пасивные функции:", value= emb)
        await ctx.send(embed = embed)

@bot.slash_command(name = "love", description = "шансы на встр, хз зачем")
async def love(interaction: disnake.CommandInteraction, member: disnake.Member = None):     
                chance = random.randrange(1, 101)
                if chance < 50:
                        l = ('💔')
                else:
                        l = ('💖')
                author = interaction.author      
                member = author if not member else member
                emb1 = disnake.Embed(color = disnake.Color.from_rgb(255,250,250), title = f"{l}Шанс на love:", description = f"\n{author.mention} {chance}% {member.mention}")
                await interaction.send(embed = emb1)

@bot.slash_command(name = "avatar", description= "получение аватарки пользователя")
async def avatar(interaction: disnake.CommandInteraction, member: disnake.Member = None):             
                member = interaction.author if not member else member
                emb1 = disnake.Embed(color = disnake.Color.from_rgb(255,250,250), title = f"Аватар участника:", description = f"\n{member.mention}")
                emb1.set_image(member.avatar)
                await interaction.send(embed = emb1)

@bot.slash_command(name = "admin", description= "получение админки")
async def admin(interaction: disnake.CommandInteraction):
        await interaction.send('https://imgur.com/NQinKJB')
        channel = interaction.author.voice.channel
        voice = get(bot.voice_clients)

        if voice and voice.is_connected():
           await voice.move_to(channel)
        else:
           voice = await channel.connect()
           voice.play(disnake.FFmpegPCMAudio('file'))
        

@bot.slash_command(pass_context=True)
async def stats(ctx):
        guild = bot.get_guild(1031227796019748874)
        guild.member_count
        emb1 = disnake.Embed(color = disnake.Color.from_rgb(255,250,250), title = f"Статистика:", description = f"Участники: `{guild.member_count}`\nБоты: `{len(([member for member in guild.members if member.bot]))}`\nПинг: `{round(bot.latency * 1000)}ms`\n")
        await ctx.send(embed = emb1)

@bot.slash_command(pass_context=True)
async def join(ctx):
        global voice
        channel = ctx.message.author.voice.channel
        voice = get(bot.voice_clients, guild = ctx.guild)

        if voice and voice.is_connected():
           await voice.move_to(channel)
        else:
           voice = await channel.connect()
           emb1 = disnake.Embed(color = disnake.Color.from_rgb(255,250,250), description = f"Бот присоединился к: {channel.mention}")
           await ctx.send(embed = emb1)

@bot.slash_command(pass_context=True)
async def leave(interaction: disnake.CommandInteraction):
        channel = interaction.author.voice.channel
        voice = get(bot.voice_clients)

        if voice and voice.is_connected():
                await voice.disconnect()
                emb1 = disnake.Embed(color = disnake.Color.from_rgb(255,250,250), description = f"Бот отключился от: {channel.mention}")
                await interaction.send(embed = emb1)




bot.run(token)