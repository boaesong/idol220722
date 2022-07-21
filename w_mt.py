import discord

intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready(): # 봇이 실행되면 한 번 실행됨
    print("이 문장은 Python의 내장 함수를 출력하는 터미널에서 실행됩니다\n지금 보이는 것 처럼 말이죠")
    await client.change_presence(status=discord.Status.online, activity=discord.Game("봇의 상태매세지"))

@client.event
async def on_message(message):
    if message.content == "신청":
        ch = client.get_channel(998976974884192296)
        await ch.send ("{} 님이 점령전 신청".format(message.author.mention))
        await message.author.send ("{}, 점령전 신청 완료, 취소는 문의방에 남겨주세요 ㅎ_ㅎ ".format(message.author, message.author.mention))
        await message.channel.purge(limit=1)


# 봇을 실행시키기 위한 토큰을 작성해주는 곳
client.run('')
