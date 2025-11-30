import os
import discord
from discord.ext import tasks, commands
import datetime

# ★ Render 환경 변수로부터 디스코드 봇 토큰 가져오기
TOKEN = os.environ.get("TOKEN")

# ★ 알림 보낼 채널 ID
CHANNEL_ID = 1444710933124354158  # 여기는 본인 채널 ID 그대로 사용

# ★ 인텐트 설정
intents = discord.Intents.default()
intents.message_content = True  # 메시지 내용 읽기/보내기 위해 필요

# ★ 봇 생성
bot = commands.Bot(command_prefix="!", intents=intents)

# ★ 한국 시간대 설정 (UTC+9)
KST = datetime.timezone(datetime.timedelta(hours=9))

# -----------------------------
#  ⚡ 봇 이벤트
# -----------------------------
@bot.event
async def on_ready():
    print(f"봇 로그인 완료: {bot.user}")

    # send_daily_message가 이미 실행중인지 체크 후 실행
    if not send_daily_message.is_running():
        send_daily_message.start()


# -----------------------------
#  ⚡ 9시 정각 자동 메시지
# -----------------------------
@tasks.loop(time=datetime.time(hour=9, minute=0, tzinfo=KST))
async def send_daily_message():
    channel = bot.get_channel(CHANNEL_ID)

    if channel:
        await channel.send("좋은아침! 출력 테스트 부하형 !")
    else:
        print("❌ 채널을 찾을 수 없습니다!")


# -----------------------------
#  ⚡ 명령어: !test
# -----------------------------
@bot.command()
async def test(ctx):
    await ctx.send("테스트 알림 도착! ✔")


# -----------------------------
#  ⚡ 봇 실행
# -----------------------------
bot.run(TOKEN)
