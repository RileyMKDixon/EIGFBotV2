#Project: EIGF Discord Bot
#Author: Riley Dixon
#Version: v0.1
#Purpose:
#Changelog:
# v0.1 - Create stub, this is the entry point for the process.

#Initialize the bot and Environment Vars here. Player data should be loaded
#in the initialization of the bot.

import os
from eigf_bot import EIGFBot
from dotenv import load_dotenv

load_dotenv()

botToken = os.getenv("EIGF_BOT_TOKEN")

bot = EIGFBot(botToken)

bot.startup()