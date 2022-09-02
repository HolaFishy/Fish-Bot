import discord
from discord.ext import commands
from main import prefix, Developers
from datetime import datetime
from discord.ext.commands import *

class Dev(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def join(self, ctx, server: int):
        me = self.client.get_user(448645983748882442)
        if ctx.author.id == me.id:
            server = self.client.get_guild(server)
            invite = await server.text_channels[0].create_invite(reason="Joining for support")
            await me.send(invite)

    @commands.command()
    async def servers(self, ctx):
        me = self.client.get_user(448645983748882442)
        if ctx.author.id == me.id:
            servers = self.client.guilds
            embed = discord.Embed(title=f"__**My Servers:**__", color=0x225c9a)
            for server in servers:
                if server.unavailable:
                    embed.add_field(name=f"{server.name} (Error)" , value=f"> (ID: `{server.id}`)", inline=True)
                    continue
                embed.add_field(name=f"{server.name} (Members: {server.member_count})" , value=f"> (ID: `{server.id}`)", inline=True)
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Dev(client))