import os
import discord
from discord.ext import tasks, commands
import datetime

# ================== 🔥 Flask 웹서버 (Render용 keep-alive) ================== #
from flask import Flask
from threading import Thread

app = Flask(__name__)  # 이름 아무거나 상관 없음

@app.route("/")
def home():
    return "Discord bot is alive!"

def run():
    # ⚠️ Render가 내부에서 PORT 환경변수를 줌 → 반드시 이걸 써야 포트 감지됨
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

def keep_alive():
    t = Thread(target=run)
    t.daemon = True
    t.start()
# ======================================================================== #


# ================== 🔥 디스코드 봇 설정 ================== #

# Render 환경 변수에서 봇 토큰 가져오기
TOKEN = os.environ.get("TOKEN")

# 알림 보낼 채널 ID (네가 쓰던 숫자 그대로 넣기)
CHANNEL_ID = 14447109933124354158  # 여기만 네 채널 ID로 유지

# 인텐트 설정
intents = discord.Intents.default()
intents.message_content = True  # 메시지 내용 읽기/보내기 위해 필요

# 봇 생성
bot = commands.Bot(command_prefix="!", intents=intents)

# 한국 시간대 (UTC+9)
KST = datetime.timezone(datetime.timedelta(hours=9))

# ------------------ 이벤트 ------------------ #
@bot.event
async def on_ready():
    print(f"✔ 봇 로그인 완료: {bot.user}")
    # 자동 메시지 루프 중복 실행 방지
    if not send_daily_message.is_running():
        send_daily_message.start()

# 아침 9시 자동 메시지
@tasks.loop(time=datetime.time(hour=9, minute=0, tzinfo=KST))
async def send_daily_message():
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        await channel.send("⏰ 좋은 아침! 출석 체크 ✅ 하세요~ !")
    else:
        print("❌ 채널을 찾을 수 없습니다!")

# 테스트 명령어
@bot.command()
async def test(ctx):
    await ctx.send("✔ 테스트 알림 도착! /ᐠ. .ᐟ\\")

# ================== 🔥 실행 순서 중요 ================== #

# 1) 웹서버 먼저 켜서 Render가 포트를 감지하게 함
keep_alive()

# 2) 그 다음 디스코드 봇 실행 (이게 메인 루프)
bot.run(TOKEN)
