import discord
from discord.ext import tasks, commands
import datetime

TOKEN = "여기에_네_토큰_넣기"
CHANNEL_ID = 1444710933124354158

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

KST = datetime.
