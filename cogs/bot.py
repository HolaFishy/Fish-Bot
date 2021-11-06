import discord
from discord.ext import commands
from main import prefix, Developers
import os
import asyncio
from datetime import datetime
from discord.ext.commands import *

class Events(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Simple on ready command, prints when the bot goes online.
    @commands.Cog.listener()
    async def on_ready(self):
        channel = self.client.get_channel(904918322318045224)
        image = self.client.get_user(797534062721368135)
        time = str(datetime.now())
        embed = discord.Embed(title=f"Fishbot has gone online!", color=discord.Color.green())
        embed.set_footer(text=f"{time[:16]}", icon_url=image.avatar.url)
        await channel.send(embed=embed)
        print(f"Bot is now online!")

    # Tells the user the bots prefix when the ping it.
    @commands.Cog.listener()
    async def on_message(self, message):
        mentions = ["@Fish Bot#7968", "<@797534062721368135>", "<@!797534062721368135>"]
        if message.content in mentions:
            embed = discord.Embed(title=f"My prefix is: {prefix[0]}", description="*You may also mention me instead of using a prefix*", color=0x225c9a)
            await message.channel.send(embed=embed, delete_after=10)
        if message.content.startswith("?mikeal myers"):
            if message.author.id == 448645983748882442:
                await message.channel.send("MEEEKYELL MYERESE")

    # SUPPORT SERVER STUFF
    # Sends a message in the channel I have specified, saying when someone has added fishbot to their server
    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        channel = self.client.get_channel(903859304090710016)
        embed = discord.Embed(title=f"{guild.name} has added Fish Bot to their server!", description=f"{guild.name}'s Description: ```\n{guild.description}\n```", 
        color=0x225c9a)
        embed.set_thumbnail(url=guild.icon.url)
        invite = await guild.text_channels[0].create_invite(reason="Creating an invite for support server (discord.gg/G8XEhAkpnj)!")
        embed.set_footer(text=f"Member Count: {guild.member_count}, Owner: {guild.owner}\nServer Invite Link: {invite}")
        await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        guild = member.guild
        MemberRole = discord.utils.get(member.guild.roles, name="Member")
        if guild.id == 900257936713076736:
            await member.add_roles(MemberRole, reason=f"Giving {member} the member role.")
            channel = self.client.get_channel(900257936713076739)
            message = await channel.send(member.mention)
            await message.delete()
            dev = self.client.get_user(448645983748882442)
            embed = discord.Embed(title=f"Welcome {member.name}!", color=0x225c9a)
            embed.add_field(name=f"If you need any help you can give **{dev.name}** a ping with your question :D", inline = False)
            await channel.send(embed=embed)
    # SUPPORT SERVER STUFF ^
    
    # WARNING THIS EVENT REMOVES FULL TRACEBACKS FROM YOUR CONSOLE, AND WILL ONLY SHOW DISCORD PROVIDED ERRORS
    '''
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        channel = self.client.get_channel(903065937312366653)
        await channel.send(f"```\n{error}\n```")
        print(error)
        embed=discord.Embed(title=f"❌ Error!", description=f"`{error}`", color=0xFF0000)
        try:
            message = await ctx.reply(embed=embed, mention_author=False)
        except:
            try:
                message = await ctx.send(embed=embed, mention_author=False)
            except:
                message = await ctx.author.send(embed=embed, mention_author=False)
        await message.add_reaction("🗑️")
        def check(reaction, user):
            return user != self.client.user and str(reaction) == "🗑️"
        try:
            reaction, user = await self.client.wait_for('reaction_add', timeout=120.0, check=check)
        except asyncio.TimeoutError:
            await message.delete()
        if str(reaction) == "🗑️":
            await message.delete()
    '''
            
class Commands(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def test(self, ctx):
        print(datetime.time)

    @commands.command(aliases=["ping","info","files"])
    async def stats(self, ctx):
        # Creates variables for the embed. (The bots users, amount of guilds the bot is in, and the guild names)
        guildAmt = 0
        guilds = []
        userCount = 0
        for guild in self.client.guilds:
            guildAmt += 1
            userCount += guild.member_count
            guilds.append(f"**{guild.name}**: {guild.member_count}")
        guilds = (", ").join(guilds)

        cogsAmt = 1
        for filename in os.listdir("./cogs"):
            if filename.endswith(".py"):
                cogsAmt += 1

        embed = discord.Embed(title=f"📊 __**{self.client.user.name}'s Stats**__", color=0x225c9a)
        embed.add_field(name=f"Bot's Ping:", value=f"<:ping:900232699015467048> {round(self.client.latency * 1000)} ms", inline = False)
        embed.add_field(name=f"Servers:", value=f"<:servers:900232712693108746> {guildAmt}", inline = False)
        embed.add_field(name=f"Bot's Users:", value=f"<:members:900233507765354557> {userCount}", inline = False)
        embed.add_field(name=f"Discord.py Version:", value=f"<:discordpy:900242452030578738>  {discord.__version__}", inline = False)
        embed.add_field(name=f"File Amount: ", value=f"<:files:900235800158011392> {cogsAmt}", inline = False)
        # Checks if the user is a dev, and if they are provides the guild names in the embed.
        if ctx.author.id in Developers:
            embed.add_field(name=f"Guilds:", value=f"> {guilds}", inline = False)
        await ctx.reply(embed=embed, mention_author=False)

    @commands.command()
    # 60 second cooldoown, per user
    @commands.cooldown(1, 60, commands.BucketType.user)
    async def suggest(self, ctx, *, suggestion=None):
        SuggestionChannel = self.client.get_channel(902285665281134652)
        # If the user messes up the command, the cooldown isn't triggered.
        if suggestion == None:
            ctx.command.reset_cooldown(ctx)
            embed=discord.Embed(title=f"❌ You must enter a message to suggest to my developer!", description=f"`{prefix[0]}suggest <suggestion>`", color=0xFF0000)
            await ctx.reply(embed=embed, mention_author=False)
            return
        await ctx.message.add_reaction("✅")
        embed=discord.Embed(title=f"Suggestion sent!", description=f"Your suggestion was sent! `{suggestion}`", color=0x225c9a)
        embed.set_footer(text=f"People may vote on your suggestion in my support server! {prefix[0]}support")
        await ctx.reply(embed=embed, mention_author=False)
        devembed = discord.Embed(title=f"{ctx.author} made a suggestion!", description=f"```{suggestion}```", color=0x225c9a)
        devembed.set_thumbnail(url=ctx.author.avatar.url)
        message = await SuggestionChannel.send(embed=devembed, mention_author=False)
        await message.add_reaction("⬆️")
        await message.add_reaction("⬇️")

    # the cooldown for the "suggest" function
    @suggest.error
    async def suggest_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            embed = discord.Embed(title=f"Command is on cooldown!",description=f"Try again in {error.retry_after:.2f}s.", color=0x225c9a)
            await ctx.reply(embed=embed, mention_author=False)
        else:
            print(error)

    # DMs the user all of the support links. (DMs so it doesn't advertise in a server that doesn't want it)
    @commands.command(aliases=["server", "bot", "invite", "website", "site"])
    async def support(self, ctx):
        embed = discord.Embed(title="__My Links!__", color=0x225c9a)
        embed.add_field(name="Support server invite:", value="> https://discord.gg/G8XEhAkpnj", inline=False)
        embed.add_field(name="My invite link:", value="> https://discord.com/api/oauth2/authorize?client_id=797534062721368135&permissions=8&scope=bot",
        inline=False)
        embed.add_field(name="All the source code for this bot!:", value="> https://github.com/sandydude/Fish-Bot", inline=False)
        embed.set_footer(text="If you need to contact my developer, join the discord support server and give him a ping!", icon_url=ctx.author.avatar.url)
        await ctx.message.add_reaction("✅")
        await ctx.author.send(embed=embed, mention_author=False)

def setup(client):
    client.add_cog(Events(client))
    client.add_cog(Commands(client))
