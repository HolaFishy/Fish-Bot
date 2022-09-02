import discord
from discord.ext import commands
from discord.ext.commands import *
import random

class Images(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def fish(self, ctx):
        fish = [
            "https://cdn.discordapp.com/attachments/913219115412492349/913219127823446066/step_6-clownfish-596f711ac4124400102014c2.png",
            "https://cdn.discordapp.com/attachments/913219115412492349/913219260728352768/s-l400.png",
            "https://cdn.discordapp.com/attachments/913219115412492349/913219297571123240/5e0f7d7520f0dc9293767f314f4bb0a1.png",
            "https://media.discordapp.net/attachments/913219115412492349/913219381872431134/787a5f19d82c0b7261ba2549e05e27c2--cute-fish-pretty-fish.png",
            "https://cdn.discordapp.com/attachments/913219115412492349/913219465699815464/XxQRB7Jf_400x400.png",
            "https://cdn.discordapp.com/attachments/913219115412492349/913220117192650803/goldfish-files.png",
            "https://cdn.discordapp.com/attachments/913219115412492349/913220281890377830/the-cute-jellyfish.png",
            "https://cdn.discordapp.com/attachments/913219115412492349/913220351553581066/PymMFbjBil5-vQTE6gif5HHv7ZrcYAauUjpWYArnIv4.png",
            "https://cdn.discordapp.com/attachments/913219115412492349/913220586946326588/happy-gold-parrot-fish-in-aquarium-picture-id177339466.png",
            "https://cdn.discordapp.com/attachments/913219115412492349/913220702201606155/54a0faf2033a7e58429a537824a52532.png",
            "https://cdn.discordapp.com/attachments/913219115412492349/913221031198601246/dixuir-bea75640-6cc8-428b-93e0-ed1992a1c2ae.png",
            "https://cdn.discordapp.com/attachments/913219115412492349/913221093635002408/eb99fc761705e013d3efaf0422ce54cf--pretty-fish-beautiful-fish.png",
            "https://cdn.discordapp.com/attachments/913219115412492349/913221205174132736/underwater-cute-salt-water-porcupine-balloonfish-fish-smiling-picture-id638309968.png",
            "https://cdn.discordapp.com/attachments/913219115412492349/913221335898001469/Clownfish.png",
            "https://cdn.discordapp.com/attachments/913219115412492349/913221476721766400/204008629_5c0e694cb2_b.png",
            "https://cdn.discordapp.com/attachments/913219115412492349/913221564865085460/fish-aquarium-underwater-sea-creatures.png",
            "https://cdn.discordapp.com/attachments/913219115412492349/913221681953247232/17429.png",
            "https://cdn.discordapp.com/attachments/913219115412492349/913221739377479810/Copperband-butterflyfish-Chelmon-rostratus-with-a-posteriorly-located-eyespot-and-a_Q320.png",
            "https://cdn.discordapp.com/attachments/913219115412492349/913221873234489395/6581.png",
            "https://cdn.discordapp.com/attachments/913219115412492349/913221931002650664/animal-cute-fish-green-Favim.png",
            "https://cdn.discordapp.com/attachments/913219115412492349/913222038771105842/betta-3229236_1920-1024x682.png",
            "https://cdn.discordapp.com/attachments/913219115412492349/913222172204490762/betum-fish-fighting-fish-betta-fish.png",
            "https://cdn.discordapp.com/attachments/913219115412492349/933848303865569372/photo-1550016728-6e898923de4c.png",
            "https://cdn.discordapp.com/attachments/913219115412492349/933848407590715402/schooling-aquarium-fish.png",
            "https://cdn.discordapp.com/attachments/913219115412492349/933848470756946010/discus-main-152406857.png",
            "https://cdn.discordapp.com/attachments/913219115412492349/933848585253031946/aquarium-fish-500x500.png",
            "https://cdn.discordapp.com/attachments/913219115412492349/933848811850301490/30d545b333151ecec49084bc5535b6db.png",
            "https://media.discordapp.net/attachments/913219115412492349/933848901180604476/purple-betta-fish_GracePhotos_Shutterstock.png",
            "https://media.discordapp.net/attachments/913219115412492349/933849146446712912/Cool-fish-names-SN-long.png",
            "https://cdn.discordapp.com/attachments/913219115412492349/933849224636940338/3bcf88f0ed127de2d1e9f8fb480892bb.png",
            "https://cdn.discordapp.com/attachments/913219115412492349/933849292999905360/lg-glofish-galactic-purple-tetra.png",
            "https://cdn.discordapp.com/attachments/913219115412492349/933849397635186758/e1ed640ea62cf1e5945519659aa1ead2.png",
            "https://cdn.discordapp.com/attachments/913219115412492349/933849558667133018/feb43ab9be2d0e2ac60d7cbb66608781.png",
            "https://media.discordapp.net/attachments/913219115412492349/933851228029485076/59cca751021189dc062b840d17698288.png?width=448&height=671"
        ]
        message = ["Bloop Bloop!", "Fishy!", "Pop!"]
        embed = discord.Embed(title=random.choice(message), color=0x225c9a)
        embed.set_image(url=random.choice(fish))
        await ctx.reply(embed=embed, mention_author=False)

def setup(client):
    client.add_cog(Images(client))