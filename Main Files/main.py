import discord
import asyncio
import time
from config import token

client = commands.Bot(command_prefix="!", case_insensitive=True)
client.remove_command("help")

@client.event
async def on_ready():
  print("I'm connected to Discord!")
  print("Currently running with the User ID: %s" % client.user.id)
  
@client.event
async def on_message(message):
  if message.content.upper() == "!PING":
    await message.channel.send(":ping_pong: Pong! I'm accepting message events now.") # This is temporary and will be replaced soon.
    
client.run(token)
