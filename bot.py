import discord
from discord.ext import commands

import os

client = commands.Bot(command_prefix = ".")
client.remove_command('help')

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='Alt Gen | .help | v5,7'))

    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('.shop'):
        embed=discord.Embed(title="Click me to go to our alt shop!", url="https://Selly.gg/@Refresh", color=0x3498db)
        embed.set_author(name="Refresh Alts", icon_url="https://cdn.discordapp.com/avatars/509798730942382080/9b2a0235965da5f7b06503fbbddad025.png?size=512")
        embed.add_field(name="for more info type '.help'", value="^^^^^^^^^^^^^^^^^^^^^^", inline=False)
        embed.set_footer(text="Refresh Alts © 2018 | all rights reserved",icon_url= "https://cdn.discordapp.com/avatars/509798730942382080/9b2a0235965da5f7b06503fbbddad025.png?size=512")
        await client.send_message(message.channel, embed=embed)

    elif message.content.startswith('.invite'):
        embed=discord.Embed(title="Click me to invite me to your own server!", url="https://discordapp.com/oauth2/authorize?&client_id=509798730942382080&scope=bot&permissions=8", color=0x3498db)
        embed.set_author(name="Refresh Alts", icon_url="https://cdn.discordapp.com/avatars/509798730942382080/9b2a0235965da5f7b06503fbbddad025.png?size=512")
        embed.add_field(name="for more info type '.help'", value="^^^^^^^^^^^^^^^^^^^^^^", inline=False)
        embed.set_footer(text="Refresh Alts © 2018 | all rights reserved",icon_url= "https://cdn.discordapp.com/avatars/509798730942382080/9b2a0235965da5f7b06503fbbddad025.png?size=512")
        await client.send_message(message.channel, embed=embed)

    elif message.content.startswith('.help'):
        embed=discord.Embed(title="here are all my commands!", color=0x3498db)
        embed.set_author(name="Refresh Alts", icon_url="https://cdn.discordapp.com/avatars/509798730942382080/9b2a0235965da5f7b06503fbbddad025.png?size=512")
        embed.add_field(name=".minecraft", value="Gives you a free minecraft alt!", inline=False)
        embed.add_field(name=".shop", value="Gives the link to our Alt shop!", inline=False)
        embed.add_field(name=".invite", value="Invite me to your own server!", inline=False)
        embed.add_field(name=".help", value="Showes this message", inline=False)
        embed.set_footer(text="Refresh Alts © 2018 | all rights reserved",icon_url= "https://cdn.discordapp.com/avatars/509798730942382080/9b2a0235965da5f7b06503fbbddad025.png?size=512")
        await client.send_message(message.channel, embed=embed)
        
client.run(os.environ["BOT_TOKEN"])
