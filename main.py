import discord
import os
import asyncio
from discord.ext import commands
from discord.ext.commands.errors import *

Developers = {
    448645983748882442 : "Hola_Fishy"
}

# The bots settings
prefix = [">", "@Fish Bot#7968 ", "<@797534062721368135> ", "<@!797534062721368135> ","@Fish Bot#7968", "<@797534062721368135>", "<@!797534062721368135>"]
game = discord.Game("with other bots!")
client = commands.Bot(
    intents= discord.Intents.all(),
    command_prefix = prefix,
    help_command = None,
    status=discord.Status.online, activity=game
    )

# Loads the cog
@client.command()
async def load(ctx, extension=None):
    if extension != None:
        extension = extension.lower()
    if ctx.author.id in Developers:
        if extension == "all" or extension == "*" or extension == None:
            for file in os.listdir("./cogs"):
                if file.endswith(".py"):
                    try:
                        client.unload_extension(f"cogs.{file[:-3]}")
                    except ExtensionNotLoaded:
                        continue
            embed = discord.Embed(title=f"📥 **All cogs loaded!**", color=0x225c9a)
            await ctx.reply(embed=embed, mention_author=False)
            return
        try:
            client.load_extension(f"cogs.{extension}")
            embed = discord.Embed(title=f"📥 **{extension} loaded**", color=0x225c9a)
            await ctx.reply(embed=embed, mention_author=False)
        except (ExtensionNotFound, ExtensionAlreadyLoaded):
            await ctx.reply("Extension not found/Is already loaded!", delete_after=5, mention_author=False)
            await asyncio.sleep(5)
            await ctx.message.delete()
    else:
        embed = discord.Embed(title=f"❌ You must be a developer to use this command!", color=0x225c9a)
        await ctx.reply(embed=embed, delete_after=15, mention_author=False)

# Unloads the cog
@client.command()
async def unload(ctx, extension=None):
    if extension != None:
        extension = extension.lower()
    if ctx.author.id in Developers:
        if extension == "all" or extension == "*" or extension == None:
            for file in os.listdir("./cogs"):
                if file.endswith(".py"):
                    try:
                        client.unload_extension(f"cogs.{file[:-3]}")
                    except ExtensionNotLoaded:
                        continue
            embed = discord.Embed(title=f"📤 **All cogs unloaded!**", color=0x225c9a)
            await ctx.reply(embed=embed, mention_author=False)
            return
        try:
            client.unload_extension(f"cogs.{extension}")
            embed = discord.Embed(title=f"📤 **{extension} unloaded**", color=0x225c9a)
            await ctx.reply(embed=embed, mention_author=False)
        except (ExtensionNotFound, ExtensionNotLoaded):
            await ctx.reply("Extension not found/Is already unloaded!", delete_after=5, mention_author=False)
            await asyncio.sleep(5)
            await ctx.message.delete()
    else:
        embed = discord.Embed(title=f"❌ You must be a developer to use this command!", color=0x225c9a)
        await ctx.reply(embed=embed, delete_after=15, mention_author=False)

# Unloads the cog, then reloads it.
@client.command()
async def reload(ctx, extension=None):
    if extension != None:
        extension = extension.lower()
    if ctx.author.id in Developers:
        if extension == "all" or extension == "*" or extension == None:
            for file in os.listdir("./cogs"):
                if file.endswith(".py"):
                    try:
                        client.unload_extension(f"cogs.{file[:-3]}")
                        client.load_extension(f"cogs.{file[:-3]}")
                    except ExtensionNotLoaded:
                        client.load_extension(f"cogs.{file[:-3]}")
            embed = discord.Embed(title=f"🔄 **All cogs reloaded!**", color=0x225c9a)
            await ctx.reply(embed=embed, mention_author=False)
            return
        try:
            try:
                client.unload_extension(f"cogs.{extension}")
                client.load_extension(f"cogs.{extension}")
                embed = discord.Embed(title=f"🔄 **{extension} reloaded**", color=0x225c9a)
                await ctx.reply(embed=embed, mention_author=False)
            except ExtensionNotLoaded:
                client.load_extension(f"cogs.{extension}")
                embed = discord.Embed(title=f"🔄 **{extension} reloaded**", color=0x225c9a)
                await ctx.reply(embed=embed, mention_author=False)
        except ExtensionNotFound:
            await ctx.reply("Extension not found!", delete_after=5, mention_author=False)
            await asyncio.sleep(5)
            await ctx.message.delete()
    else:
        embed = discord.Embed(title=f"❌ You must be a developer to use this command!", color=0x225c9a)
        await ctx.reply(embed=embed, delete_after=15, mention_author=False)

# Loads all the cogs when the bot is run
for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")

client.run("token")
