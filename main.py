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

def get_ai_reply(username, message):
    try:
        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=f"Tum Foxy naam ka Discord bot ho. Hindi me reply karo.\nUser: {username}\nMessage: {message}"
        )
        return response.text
    except Exception as e:
        print(e)
        return "AI unavailable."

@bot.event
async def on_ready():
    print(f"Foxy Gemini Online: {bot.user}")

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    reply = get_ai_reply(message.author.name, message.content)
    await message.reply(reply)

bot.run(DISCORD_TOKEN)
