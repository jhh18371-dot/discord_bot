import os
import discord
from discord.ext import tasks, commands
import datetime

# ✔ Render 환경 변수로부터 디스코드 봇 토큰 가져오기
TOKEN = os.environ.get("TOKEN")

# ✔ 알림 보낼 채널 ID
CHANNEL_ID = 14447109933124354158  # 네가 쓰던 채널 ID

# ✔ 인텐트 설정
intents = discord.Intents.default()
intents.message_content = True  # 메시지 내용 읽기/보내기 위해 필요

# ✔ 봇 생성
bot = commands.Bot(command_prefix="!", intents=intents)

# ✔ 한국 시간대 설정 (UTC+9)
KST = datetime.timezone(datetime.timedelta(hours=9))


# 🔥 봇 이벤트
@bot.event
async def on_ready():
    print(f"✔ 봇 로그인 완료: {bot.user}")
    # 자동 메시지 루프 시작 (중복 방지)
    if not send_daily_message.is_running():
        send_daily_message.start()


# 🔥 아침 9시 자동 메시지
@tasks.loop(time=datetime.time(hour=9, minute=0, tzinfo=KST))
async def send_daily_message():
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        await channel.send("⏰ 좋은아침! 출석 체크✅ 하세요~ !")
    else:
        print("❌ 채널을 찾을 수 없습니다!")

def run():
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
    
# 🔥 테스트 명령어
@bot.command()
async def test(ctx):
    await ctx.send("✔ 테스트 알림 도착! /ᐠ. .ᐟ\\")
 

# 🔥 봇 실행
bot.run(TOKEN)
