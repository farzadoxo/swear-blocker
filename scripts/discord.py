# Discord.py version

from discord.ext import commands
from discord import Intents , Message

client = commands.Bot(command_prefix="!",
                      intents=Intents.default())


swears = ['fuck','bitch'] # List of swears and bad words

@client.event #Setup event when a message send
async def on_message(message:Message):
    if message.content in swears:
        await message.channel.send("This text itself is a curse.!!!")
    else:
        counter = 0 #To prevent consecutive responses for texts containing several swear words
        word = message.content.split(' ') # list words by ' ' (space) 
        for i in word:
            for j in swears:
                if i == j:
                    counter += 1 
                    # But you can use 'Break' !
                    if counter == 1:
                        await message.channel.send("This text contains bad words!")





client.run("Your token")