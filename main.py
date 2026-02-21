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
    print(f"✅ Foxy Gemini Ultimate Online: {bot.user}")

def ask_gemini(username, message):
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=f"Tum Foxy naam ka Discord bot ho. Hindi me reply karo.\nUser: {username}\nMessage: {message}"
        )

        return response.text

    except Exception as e:
        print("Gemini Error:", e)
        return "⚠️ AI temporary unavailable hai."

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    reply = ask_gemini(message.author.name, message.content)
    await message.reply(reply)

bot.run(DISCORD_TOKEN)
