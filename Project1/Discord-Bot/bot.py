import os

import discord
import random
from dotenv import load_dotenv

load_dotenv()
#print(os.getenv('DISCORD_TOKEN'))
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    coffeebrewer_quotes = [
        'Remember to get your hourly cup of coffee!',
        'There you go, champ!',
        'You have made a critical mistake, and that is you thinking that anything can be done before a nice cup of joe!',
        (
            'Here you go, boss! Fresh out of the pot!'
        ),
    ]
    
    if message.content == 'Coffee!':
        response = random.choice(coffeebrewer_quotes)
        await message.channel.send(response)

client.run(TOKEN)
