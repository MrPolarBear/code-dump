################IMPORTS####################
import os
import discord
import random
import requests, json
import pyowm
import random
##########################################


####################################
from dotenv import load_dotenv
from datetime import datetime
from discord.ext.commands import Bot
from discord.ext.commands import command
from discord.ext.commands import Cog
from discord.ext import commands
from random import randrange
from discord import Embed, Member

load_dotenv()
# GET TOKEN
TOKEN = 'Nzk0ODM3MzQ0NTQ0NDg5NTEy.X_An9g.z18P7hXbaZJOjoyQz2V_CQNPfNU'
GUILD = os.getenv('DISCORD_GUILD')
BOT_PREFIX = ("!", "?")

client = discord.Client()

bot = commands.Bot(command_prefix="!")


####################################
# Interactive commands with EQ-BOT


@client.event

async def on_message(message):
    #added
    target= message.author
    name = str(target)

    #ITEMS
    lights = [
            "<:feelsblyat:664298254363656193> Weak Flashlight <:feelsblyat:664298254363656193>", 
            "<:GachiGasm:586355105700380684> Strong Flashlight <:GachiGasm:586355105700380684>",
            "<:pepeok:586350215464747060> Candle <:pepeok:586350215464747060>", 
            "<:kekw:664292527184019467> Fuckin Lighter lmao <:kekw:664292527184019467>", 
            "<:pepecry:759927141683953696> Glow Dildo <:pepecry:759927141683953696>", 
            "<:pepelaugh:586353889717256192> REVEAL CUM LIGHT <:pepelaugh:586353889717256192>"]
    items = ["EMF Reader",  "Photo Camera", "Crucifix", "Video Camera", "Spirit Box", "Salt", "Smudge Sticks", "Tripod/Camera",  "Motion Sensor", "Sound Sensor", "Thermometer", "Ghost Writing Book", "Infrared Light Sensor", "Parabolic Microphone"]
    roles = ["Priest", "Camera Man", "Scout", "Speaker"]
    #CHOICES
    choice = ["Yes", "No"]
    allowsan = choice[randrange(2)]
    allowlight = choice[randrange(2)]
    allowsprint = choice[randrange(2)]
    allowhiding = choice[randrange(2)]
    allowrsupply = choice[randrange(2)]
    headmount = choice[randrange(2)]
    lightrng=random.randint(0,5)
    lightrng2=random.sample(range(0,5),4)
    itemrng=random.randint(0,13)
    itemrng2=random.sample(range(0,14),3)
    if message.author == client.user:
        return

#####################
#User Information
#####################
    if message.content.startswith('!extrarules'):
        embed= Embed(title="Additional Rules for individual player")
        fields = [("User:", str(target), False),
                  ("EXTRA CONTITIONS", "HEAD MOUNTED CAM?: " +str(headmount)
                                + "\nALLOW SANITY PILLS?: "+str(allowsan)
                                + "\nALLOW SPRINT?: "+str(allowsprint)
                                + "\nALLOW HIDING?: "+str(allowhiding), False)
                ]
        for name, value, inline in fields:       
            embed.add_field(name=name, value=value, inline=inline)
        await message.channel.send(embed=embed)
#########################
#RANDOM CHALLENGE
#########################
    if message.content.startswith('!challengerng'):
        embed = Embed(title="Phasmo RNG Challenge", description="Get ready to get fucked lmao. You get whatever RNJesus gives you. If noone on the team has a light source then idk either 1 rerolls or all suffer with no light source lul.\n**Quicknote:** Resupply applies to items with multiples of itself (ie crucifix, if no resupply then you can only bring 1)", color=0x00ff00 )
        if allowlight == "Yes":
            fields = [("Ghost Hunter:", name, False),
                      ("Light Carrier?", "<:PogU:586352332779028490> You may shine like my asshole <:PogU:586352332779028490>", False ),
                      ("Inventory:", "Light Source: " + str(lights[lightrng]) + "\nItem 1: " + str(items[itemrng2[0]]) + "\nItem 2: " + str(items[itemrng2[1]]), False),
                      ("EXTRA CONTITIONS", str("You may choose to play with these extra rules or not") 
                                + "\n\nHEAD MOUNTED CAM?: " +str(headmount)
                                + "\nALLOW SANITY PILLS?: "+str(allowsan)
                                + "\nALLOW SPRINT?: "+str(allowsprint)
                                + "\nALLOW HIDING?: "+str(allowhiding)
                                + "\nALLOW RESUPPLYING?: " + str(allowrsupply),False)
                    ]
            for name, value, inline in fields:
                embed.add_field(name=name, value=value, inline=inline)
            await message.channel.send(embed=embed)
    
        if allowlight == "No":
            fields = [("Ghost Hunter:", name, False),
                      ("Light Carrier?", "<:pepepoint:759927167248236564> Get fucked u can't see shit lmao <:pepepoint:759927167248236564>", False ),
                      ("Inventory:", "Item 1: " + str(items[itemrng2[2]]) 
                                    + "\nItem 2: "+str(items[itemrng2[0]]) 
                                    + "\nItem 3: " +str(items[itemrng2[1]]), False),
                      ("EXTRA CONTITIONS", str("You may choose to play with these extra rules or not") 
                                + "\n\nHEAD MOUNTED CAM?: " +str(headmount)
                                + "\nALLOW SANITY PILLS?: "+str(allowsan)
                                + "\nALLOW SPRINT?: "+str(allowsprint)
                                + "\nALLOW HIDING?: "+str(allowhiding)
                                + "\nALLOW RESUPPLYING?: " + str(allowrsupply),False)
                      ]
            for name, value, inline in fields:
                embed.add_field(name=name, value=value, inline=inline)
            await message.channel.send(embed=embed)

############################################
#ASSIGN ROLES CHALLENGE
############################################
    if message.content.startswith("!challengerole"):
        rollplayer=random.sample(range(0,4),4)
        embed = Embed(title="Phasmo Role Playing Challenge", description="***AMENO***\nAssign roles from top to bottom on Whiteboard in game. Each player is allowed to carry the designated light source. Do !roles to see what your role is allowed to carry. If a player dies you cannot use the items that player's role uses. If you want additional rules like challengerng then do !extrarules for each player.", color=0x00ff00 )
        fields=[("Player 1", str(roles[rollplayer[0]]) + "\nLight Source: " + str(lights[lightrng2[0]]), False),
                ("Player 2", str(roles[rollplayer[1]]) + "\nLight Source: " + str(lights[lightrng2[1]]), False),
                ("Player 3", str(roles[rollplayer[2]]) + "\nLight Source: " + str(lights[lightrng2[2]]), False),
                ("Player 4", str(roles[rollplayer[3]]) + "\nLight Source: " + str(lights[lightrng2[3]]), False)
        ]
        for name, value, inline in fields:
            embed.add_field(name=name, value=value, inline=inline)
        await message.channel.send(embed=embed)

###########################
#Roles command
###########################
    if message.content.startswith("!roles"):
        embed = Embed(title="List of Roles", description="Each role can only use these objects. If u break the fuckin rule i'll come eat your ass.", color=0x00ff00 )
        fields=[("Priest", "Crucifix, smudge sticks, salt and candles", False),
                ("Camera Man", "Any form of camera+tripods.", False),
                ("Scout", "Motion sensors, thermometer, and parabolic.", False),
                ("Speaker", "Spirit box, Spirit book, and EMF reader.", False)
        ]
        for name, value, inline in fields:
            embed.add_field(name=name, value=value, inline=inline)
        await message.channel.send(embed=embed)
############################
#Help
############################
    if message.content.startswith("!help1"):
        await message.channel.send("Suck my dick lmao"
        +"\nAll commands:"
        +"\n[!challengerole]   [!challengerng]   [!roles]   [!extrarules]")



@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('--------')


client.run(TOKEN)
bot.run(TOKEN)
