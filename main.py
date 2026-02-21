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
            "message": message,
            "ownername": "Foxy PlayzZ",
            "botname": "Foxy",
            "user": username
        }
        r = requests.get(API1, params=params, timeout=10)
        return r.json().get("message")
    except:
        return None

def ai_simsimi(message):
    try:
        params = {"text": message, "lc": "hi"}
        r = requests.get(API2, params=params, timeout=10)
        return r.json().get("message")
    except:
        return None

def get_ai_reply(user_id, username, message):
    reply = ai_affiliate(message, username)
    if not reply:
        reply = ai_simsimi(message)
    if not reply:
        reply = "Maaf kijiye, abhi AI busy hai. Thodi der baad try kare."
    return reply

@bot.event
async def on_ready():
    print(f"Ultimate Foxy v6 FREE AI Online: {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} commands")
    except Exception as e:
        print(e)

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    reply = get_ai_reply(str(message.author.id), message.author.name, message.content)
    await message.reply(reply)
    await bot.process_commands(message)

@bot.tree.command(name="ai", description="Foxy FREE AI se baat kare")
async def ai(interaction: discord.Interaction, question: str):
    await interaction.response.defer()
    reply = get_ai_reply(str(interaction.user.id), interaction.user.name, question)
    await interaction.followup.send(reply)

@bot.tree.command(name="ping", description="Bot status check kare")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("Foxy FREE AI Online hai!")

bot.run(DISCORD_TOKEN)
