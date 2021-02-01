import discord
import random
import os

client = discord.Client()
token = "ODA1NTkxMDcwOTEzMzMxMjUx.YBdHJg.A50KOV3qHtgeiKS_mUUjIU_woHk"

@client.event
async def on_ready():
    print("봇이 온라인으로 전환되었습니다.")

@client.event
async def on_message(message):
    if message.content.startswith("안녕"):
        await message.channel.send("방가워!")

    if message.content == ("?가위") or message.content == ("?바위") or message.content == ("?보"):
        bot_random = random.randint(1, 3)

    if bot_random == 1:    # random 에 저장된 변수가 1일때 (가위 일때)
        if message.content == ("?가위"):
            await message.channel.send("가위!")
            await message.channel.send("비겼어..ㅠ")

        elif message.content == ("?바위"):
            await message.channel.send("가위!")
            await message.channel.send("내가 졌어....")

        else:
            await message.channel.send("가위!")
            await message.channel.send("내가 이겼어!")

        if bot_random == 2:    # random 에 저장된 변수가 2일때 (바위 일때)
            if message.content == ("?가위"):
                await message.channel.send("바위!")
                await message.channel.send("내가 이겼어!")

            elif message.content == ("?바위"):
                await message.channel.send("바위!")
                await message.channel.send("비겼어..ㅠ")

            else:
                await message.channel.send("바위!")
                await message.channel.send("내가 졌어....")

    if bot_random == 3:    # random 에 저장된 변수가 3일때 (보 일때)
            if message.content == ("?가위"):
                await message.channel.send("보!")
                await message.channel.send("내가 졌어....")

            elif message.content == ("?바위"):
                await message.channel.send("보!")
                await message.channel.send("내가 이겼어!")

            else:
                await message.channel.send("보!")
                await message.channel.send("비겼어..ㅠ")

access_token = os.environ["BOT_TOKEN"]                
client.run(access_token)
