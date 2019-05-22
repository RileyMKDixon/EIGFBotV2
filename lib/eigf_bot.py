#Project: EIGF Discord Bot
#Author: Riley Dixon
#Class: EIGFBot
#Version: v0.1
#Purpose: The high level abstraction of the discord bot. All data requests
#         should be handled here and then passed to the cooresponding data
#         class.
#Changelog:
# v0.1 - Create stub class.


import os
import asyncio
import discord

from eigf_output.discord_outputstream import Discord_Outputstream

class EIGFBot():
    client = discord.Client()
    def __init__(self, private_token):
        self.private_token = private_token

    def startup(self):
        EIGFBot.client.loop.create_task(backgroundHeartbeatTask(EIGFBot.client))
        EIGFBot.client.run(self.private_token)
    
    @client.event
    async def on_ready():
        print("EIGF Bot Ready")
        print("Bot Name: " + EIGFBot.client.user.name)
        print("Bot ID: " + str(EIGFBot.client.user.id))

    #Need to get away from on_message and move to proper commands
    @client.event
    async def on_message(message):
        parsedMessage = message.content.split(' ')
        if(parsedMessage[0][0] == "!" and message.author != EIGFBot.client.user
            and message.author.name + "#" + message.author.discriminator == "Champion1#5795"):
            pass
            
    def close(self):
        pass

async def backgroundHeartbeatTask(client):
    await EIGFBot.client.wait_until_ready()
    while(not EIGFBot.client.is_closed):
        print("Bot is still alive!")
        await asyncio.sleep(120) #Sleep for 120 seconds
