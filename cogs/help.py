import discord
from discord.ext import commands
from main import prefix

class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    #  Help command, if the user enters a valid catagory, gives information on all the commands in a catagory
    @commands.command()
    async def help(self, ctx, *, catagory=None):
        dev = self.client.get_user(448645983748882442)
        # Default embed
        MainEmbed = discord.Embed(title="❔ Help Menu!", description=f"Valid Prefixs: `{prefix[0]}`, `@Fish Bot#7968`, `<@797534062721368135>`\
        \nTo get more information on any command, run `{prefix[0]}help <catagory>`", color = 0x225c9a)
        MainEmbed.add_field(name="⚔️ Moderation", value=f"> `ban <member> (reason)`\n> `unban <member> (reason)`\n> `muterole (creates a muted role)`\
        \n> `mute <member> <reason>`\n> `unmute <member>`\n> `kick <member> <reason>`")
        MainEmbed.add_field(name="🖨️ Text", value=f"> `clap <sentence>`\n> `mock <sentence>`\n> `upsidedown <sentence>`\n> `sparkle <sentence>`\
        \n> `fancy <sentence>`")
        MainEmbed.add_field(name="🤖 Bot Info", value=f"> `stats`\n> `support`\n> `suggest (suggestions for the bot)`")
        MainEmbed.add_field(name="📚 General Commands", value=f"> `userinfo <member>`\n> `avatar <member>`\n> `embed <title> / <description>`")
        MainEmbed.set_footer(text=f"This bot was coded in Python!\nand was developed by {dev} ❤️",
        icon_url="https://cdn.discordapp.com/emojis/898009300646105089.png?size=128")
        MainEmbed.set_author(name=f"Get more information on any command, run '{prefix[0]}help <catagory>'")

        if catagory != None:
            catagory = catagory.lower()

            # Checks if the catagory is "mod"
            if catagory.startswith("mod"):
                embed = discord.Embed(title="⚔️ Moderation", color = 0x225c9a)
                embed.add_field(name=f"`ban <member> (reason)`", value="> *Bans a member, and logs the reason in the audit logs if provided.*")
                embed.add_field(name=f"`unban <member>`", value="> *Unbans a user, you must enter the user in this format: `Username#Numbers`*")
                embed.add_field(name=f"`mute <member> (reason)`", value=f"> *Mutes a member, if you do not have a mute role create one using `{prefix[0]}muterole`*")
                embed.add_field(name=f"`muterole`", value=f"> *Creates a mute role, the role must remain named `Muted` or it will not work!*")
                embed.add_field(name=f"`kick <member> (reason)`", value=f"> *Kicks a member, and logs the reason in audit logs if provided.*")
                embed.set_footer(text="the items in '<>'s are required, the items in '()'s are optional.")
                await ctx.reply(embed=embed, mention_author=False)
            # Checks if the catagory is "text"
            elif catagory.startswith("text"):
                embed = discord.Embed(title=f"🖨️ Text", color = 0x225c9a)
                embed.add_field(name=f"`clap <sentence>`", value=f"> *Adds the 👏 emoji in-between every word: This 👏 is 👏 an 👏 example*")
                embed.add_field(name=f"`mock <sentence>`", value=f"> *Sends a message with every other capitals: ThIs Is An ExAmPlE*\
                    \n> *You may also reply to someone else message to mock their message.*")
                embed.add_field(name=f"`upsidedown <sentence>`", value=f"> *Flips a sentence upsidedown: ǝldɯɐxǝ uɐ sı sıɥʇ*")
                embed.add_field(name=f"`sparkle <sentence>`", value=f"> *Adds sparkles to to a sentence: t͓̽h͓̽i͓̽s͓̽ i͓̽s͓̽ a͓̽n͓̽ e͓̽x͓̽a͓̽m͓̽p͓̽l͓̽e͓̽*")
                embed.add_field(name=f"`fancy <sentence>`", value=f"> *Makes a sentence faaancy: 𝓉𝒽𝒾𝓈 𝒾𝓈 𝒶𝓃 𝑒𝓍𝒶𝓂𝓅𝓁𝑒*")
                await ctx.reply(embed=embed, mention_author=False)
            # Checks if the catagory is "bot info"
            elif catagory.startswith("bot"):
                embed= discord.Embed(title=f"🤖 Bot Info", color = 0x225c9a)
                embed.add_field(name=f"`suggest <suggestion>`", value=f"> *Makes a suggestion for this bot, you may vote on suggestions in my support server (`{prefix[0]}support`)*")
                embed.add_field(name=f"`stats`", value=f"> *Shows the stats of this bot*")
                embed.add_field(name=f"`support`", value=f"> *DMs the user support links*")
                embed.set_footer(text="the items in '<>'s are required, the items in '()'s are optional.")
                await ctx.reply(embed=embed, mention_author=False)
            # Checks if the catagory is "general"
            elif catagory.startswith("gen"):
                embed = discord.Embed(title=f"📚 General Commands", color = 0x225c9a)
                embed.add_field(name=f"`embed <title> / (description)`", value=f"> *Sends an embed based on the args provided. You may add a description by adding a / to seperate the two fields*")
                embed.add_field(name=f"`userinfo (member)`", value=f"> *Sends all info on the user provided, or the author if no user is provided*")
                embed.add_field(name=f"`avatar (member)`", value=f"> *Sends the avatar of the user provided, or the author if no user is provided*")
                embed.set_footer(text="the items in '<>'s are required, the items in '()'s are optional.")
                await ctx.reply(embed=embed, mention_author=False)
            else:
                # If no valid catagory is provided, sends the default embed
                await ctx.reply(embed=MainEmbed, mention_author=False)
        # If no catagory is provided, sends the default embed
        else:
            await ctx.reply(embed=MainEmbed, mention_author=False)
        
def setup(client):
    client.add_cog(Help(client))
