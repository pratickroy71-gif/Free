import discord
from discord.ext import commands
import os
import requests

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="/", intents=intents)

API1 = "https://api.affiliateplus.xyz/api/chatbot"
API2 = "https://api.simsimi.vn/v2/simtalk"

def ai_affiliate(message, username):
    try:
        params = {
            "message": str(message),
            "ownername": "Foxy PlayzZ",
            "botname": "Foxy",
            "user": str(username)
        }
        r = requests.get(API1, params=params, timeout=10)
        data = r.json()
        if "message" in data:
            return data["message"]
        return None
    except:
        return None

def ai_simsimi(message):
    try:
        params = {
            "text": str(message),
            "lc": "en"
        }
        r = requests.get(API2, params=params, timeout=10)
        data = r.json()
        if "message" in data:
            return data["message"]
        return None
    except:
        return None

def get_ai_reply(username, message):
    reply = ai_affiliate(message, username)

    if not reply:
        reply = ai_simsimi(message)

    if not reply:
        reply = "Namaste! Main Foxy hoon 😊"

    return reply

@bot.event
async def on_ready():
    print(f"Foxy FREE AI Online: {bot.user}")

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    reply = get_ai_reply(message.author.name, message.content)
    await message.reply(reply)

bot.run(DISCORD_TOKEN)
