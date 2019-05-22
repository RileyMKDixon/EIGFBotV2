#Project: EIGF Discord Bot
#Author: Riley Dixon
#Class: Discord_Outputstream
#Version: v0.1
#Purpose: Used to send messages to a particular channel in the discord
#         guild. Discord has a 2000 character limit per message, as well as
#         a cooldown of about 5 messages per second. This class will manage
#         both restrictions from output.
#Changelog:
# v0.1 - Create stub class.


class Discord_Outputstream():
    #Discord has a limit of 2000 characters per message for their API
    #There is also a limit to number of messages the bot can send in a period
    #of time. To help make the bots actions appear smoother, limiting messages
    #may be desired.
    @classmethod
    async def sendMessage(self, channel, message):
        numberOfMessageChunks = int(len(message)/2000)
        for i in range(0, numberOfMessageChunks + 1):
            await channel.send(message[i*2000:(i+1)*2000])

