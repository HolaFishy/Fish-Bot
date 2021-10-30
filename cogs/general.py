import discord
from discord import client
from discord.ext import commands
from main import prefix
import asyncio

class General(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Sends an embed, seperate the fields with a "/"
    @commands.command(aliases=["em"])
    async def embed(self, ctx, *,message=None):
        if message == None:
            embed = discord.Embed(title="❌ You must enter a message to embed!", color=0xFF0000)
            await ctx.reply(embed=embed, mention_author=False)
            return
        await ctx.message.delete()
        try:
            title, description = message.split("/")
        except:
            title = message
            description = ""
        embed = discord.Embed(title=f"{title}", description=f"{description}",color = ctx.author.color)
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar.url)
        await ctx.reply(embed=embed, mention_author=False)

    # Gets the avatar of a member
    @commands.command(aliases=["av"])
    async def avatar(self, ctx, member:discord.Member=None):
        if member == None:
            member = ctx.author
        embed = discord.Embed(title=f"**__{member}'s Avatar__**",
        description=f"[Avatar Link (PNG)]({member.avatar.url})",
        color=member.color)
        embed.set_image(url=member.avatar.url)
        message = await ctx.reply(embed=embed, mention_author=False)

    # Gives information on a user
    @commands.command(aliases=["user"])
    async def userinfo(self, ctx, member: discord.Member=None):
        if member == None:
            member = ctx.author
        
        # Title
        message = f"{member.name} ({member.id})"
        if member.bot == True:
            message = f"`BOT` {member} (ID: {member.id})"
        else:
            message = f"{member.name} (ID: {member.id})"
        embed = discord.Embed(title=message, color=member.color)
        # Status
        if member.status != None:
            embed.add_field(name=f"Status:", value=f"> `{member.status}`")
        else:
            embed.add_field(name=f"Activity:", value=f"> `Can't get user's status.`", inline=False)
        # Activity
        if member.activity != None:
            embed.add_field(name=f"Activity:", value=f"> `{member.activity}`", inline=False)
        else: 
            embed.add_field(name=f"Activity:", value=f"> `Isn't playing anything.`", inline=False)
        # Created At
        created_at = str(member.created_at)
        embed.add_field(name=f"Date of account creation:", value=f"> `{created_at[:10]}` at `{created_at[11:16]}`", inline=False)
        # Joined At
        joined_at = str(member.joined_at)
        embed.add_field(name=f"Date of server join:", value=f"> `{joined_at[:10]}` at `{joined_at[11:16]}`", inline=False)
        # Permissions
        MemberPerms = []
        AdminPermissions = [
            "kick_members", "ban_members", "administrator", "manage_channels", "manage_guild", "view_audit_log", "manage_messages",
            "mention_everyone", "mute_members", "deafen_members", "move_members", "manage_roles", "manage_emojis"
        ]
        admin = False
        for perm in member.guild_permissions:
            if perm[0] == "administrator" and perm[1] == True:
                admin = True
        if admin == True:
            MemberPerms = "`administrator` (every permission)"
        else:
            for perm in member.guild_permissions:
                if perm[0] in AdminPermissions and perm[1] == True:
                    MemberPerms.append(f"`{perm[0]}`")
            MemberPerms = (", ").join(MemberPerms)
        if MemberPerms == "":
            MemberPerms = "`No Admin Permissions`"
        embed.add_field(name=f"Administrator Permissions: ", value=f"> {MemberPerms}", inline=False)
        # Roles
        roles = []
        for role in reversed(member.roles):
            if role.name == "@everyone":
                roles.append("@everyone")
            else:
                roles.append(role.mention)
        roles = (", ").join(roles)
        embed.add_field(name=f"Roles: ", value=f"> {roles}", inline=False)
        # replying Message
        embed.set_thumbnail(url=ctx.author.avatar.url)
        await ctx.reply(embed=embed, mention_author=False)

def setup(client):
    client.add_cog(General(client))