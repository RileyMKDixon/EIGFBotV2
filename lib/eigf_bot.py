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

class EIGFBot():
    def __init__(self, private_token):
        self.private_token = private_token
        self.client = discord.Client()

    def startup(self):
        self.client.loop.create_task(backgroundHeartbeatTask(self.client))
        self.client.run(self.private_token)

    def close(self):
        pass

async def backgroundHeartbeatTask(client):
    await client.wait_until_ready()
    while(not client.is_closed):
        print("Bot is still alive!")
        await asyncio.sleep(120) #Sleep for 120 seconds
