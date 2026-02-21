import discord
from discord.ext import commands
import os
from google import genai

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=GEMINI_API_KEY)

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Foxy Gemini Online: {bot.user}")

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    try:
        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=f"Tum Foxy naam ka friendly Discord bot ho. Hindi me short reply karo.\nUser: {message.author.name}\nMessage: {message.content}"
        )

        reply = response.text

    except Exception as e:
        print(e)
        reply = "Maaf kijiye, AI abhi unavailable hai."

    await message.reply(reply)

bot.run(DISCORD_TOKEN)
