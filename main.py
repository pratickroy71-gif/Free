import discord
from discord.ext import commands
import os
import requests

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

API = "https://api.affiliateplus.xyz/api/chatbot"

def get_ai_reply(username, message):
    try:
        params = {
            "message": message,
            "ownername": "Foxy PlayzZ",
            "botname": "Foxy",
            "user": username
        }

        response = requests.get(API, params=params, timeout=10)
        data = response.json()

        if "message" in data:
            return data["message"]

    except Exception as e:
        print("AI Error:", e)

    # fallback reply
    return "Namaste! Main Foxy hoon 😊 Kaise madad kar sakta hoon?"

@bot.event
async def on_ready():
    print(f"✅ Foxy FREE AI Online: {bot.user}")

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    reply = get_ai_reply(message.author.name, message.content)
    await message.reply(reply)

bot.run(DISCORD_TOKEN)
