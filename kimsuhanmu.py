import discord
import openpyxl
import os

client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("-김수한무 도움말")
    await client.change_presence(status=discord.Status.online, activity=game)

    
@client.event
async def on_message(message):
    if message.author.bot:
        return None
    
    if message.content.startswith("-김수한무야"):
        await message.channel.send("무슨 일 이십니까?")

if message.content.startswith("-김수한무 도움말"):
        embed=discord.Embed(title="Example Embed", description="이것은 Embed입니다.", color=0x00ff56)
        embed.set_author(name="저자의 이름", url="https://blog.naver.com/huntingbear21", icon_url="https://cdn.discordapp.com/attachments/717016146716655677/717218639417442385/94ff9a0cbc761033.png")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/717016146716655677/717218639417442385/94ff9a0cbc761033.png")
        embed.add_field(name="이것은 필드입니다.", value="필드의 값입니다.", inline=True)
        embed.add_field(name="이것은 필드 2입니다.", value="필드의 값입니다.", inline=True)
        embed.add_field(name="이것은 필드 3입니다.", value="필드의 값입니다.", inline=True)
        embed.add_field(name="이것은 필드 4입니다.", value="필드의 값입니다.", inline=True)
        embed.set_footer(text="이것은 푸터입니다.")
        await message.channel.send(embed=embed)
        
    if message.content.startswith("ㅋㅋㅋ"):
        await message.channel.send("하하하하하 :)")

    if message.content.startswith(""):
        file = openpyxl.load_workbook("레벨.xlsx")
        sheet = file.active
        exp = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000]
        i = 1
        while True:
            if sheet["A" + str(i)].value == str(message.author.id):
                sheet["B" + str(i)].value = sheet["B" + str(i)].value + 2
                if sheet["B" + str(i)].value >= exp[sheet["C" + str(i)].value - 1]:
                    sheet["C" + str(i)].value = sheet["C" + str(i)].value + 1
                    await message.channel.send("레벨이 올랐습니다.\n현재 레벨 "  + str(sheet["C" + str(i)].value) + "\n경험치 : " + str(sheet["B" + str(i)].value))
                file.save("레벨.xlsx")
                break

            if sheet["A" + str(i)].value == None:
                sheet["A" + str(i)].value = str(message.author.id)
                sheet["B" + str(i)].value = 0
                sheet["C" + str(i)].value = 1
                file.save("레벨.xlsx")
                break

            i += 1

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
