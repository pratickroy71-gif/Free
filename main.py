import discord
from discord.ext import commands
import os
import google.generativeai as genai

# Load API keys
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

def get_ai_reply(message, username):
    try:
        response = model.generate_content(
            f"Tum Foxy naam ka Discord bot ho. Hindi me reply karo. User: {username}\nMessage: {message}"
        )
        return response.text
    except Exception as e:
        print(e)
        return "AI reply unavailable."

@bot.event
async def on_ready():
    print(f"✅ Foxy Gemini AI Online: {bot.user}")

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    reply = get_ai_reply(message.content, message.author.name)
    await message.reply(reply)

bot.run(DISCORD_TOKEN)
