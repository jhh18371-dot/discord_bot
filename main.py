import discord
from discord.ext import tasks, commands
import datetime

import os
TOKEN = os.environ.get("TOKEN")
CHANNEL_ID = 1444710933124354158

# 필수: 인텐트 세팅
intents = discord.Intents.default()
intents.message_content = True   # 메시지 보내기/읽기 위해 필요

bot = commands.Bot(command_prefix="!", intents=intents)

KST = datetime.timezone(datetime.timedelta(hours=9))

@bot.event
async def on_ready():
    print(f"로그인 완료: {bot.user}")
    if not send_daily_message.is_running():
        send_daily_message.start()

@tasks.loop(time=datetime.time(hour=9, minute=0, tzinfo=KST))
async def send_daily_message():
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
         await channel.send("좋은아침~ 출석체크 부탁해 !")
    else:
        print("채널을 찾을 수 없습니다!")

@bot.command()
async def test(ctx):
    await ctx.send("테스트 알림 도착! ✓")

# ★★★ 반드시 마지막! ★★★
bot.run(TOKEN)




