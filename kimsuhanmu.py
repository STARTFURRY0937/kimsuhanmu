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
        embed=discord.Embed(title="Example Embed", description="이것은 도움말 목록입니다.", color=0x00ff56)
        embed.set_author(name="제작자", url="https://www.youtube.com/channel/UClN0RrhhqXYLZlDDUNPH6Jg", icon_url="https://cdn.discordapp.com/attachments/717016146716655677/717218639417442385/94ff9a0cbc761033.png")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/717016146716655677/717218639417442385/94ff9a0cbc761033.png")
        embed.add_field(name="김수한무 게임", value="-김수한무 게임말", inline=True)
        embed.add_field(name="김수한무 대화", value="-김수한무 대화말", inline=True)
        embed.add_field(name="이것은 필드 3입니다.", value="필드의 값입니다.", inline=True)
        embed.add_field(name="이것은 필드 4입니다.", value="필드의 값입니다.", inline=True)
        embed.set_footer(text="이것은 푸터입니다.")
        await message.channel.send(embed=embed)
        
    if message.content.startswith("-김수한무 네르"):
        embed=discord.Embed(title=".뉄", description="이것은 넬.의 프로필 입니다.", color=0x00ff56)
        embed.set_author(name="네르", url="https://www.youtube.com/channel/UCf8xaoq1X55ZGnJn7kKtHwA", icon_url="https://cdn.discordapp.com/attachments/692941163920883732/717282429538140211/JPEG_20200103_190316.jpg")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/717016146716655677/717218639417442385/94ff9a0cbc761033.png")
        embed.add_field(name="이름", value="네르", inline=True)
        embed.add_field(name="주로 하는 말", value="ppap", inline=True)
        embed.add_field(name="좋아하는 게임", value="테라리아", inline=True)
        embed.add_field(name="한마디.", value="?", inline=True)
        embed.set_footer(text="이 사람은 넬. 입니다.")
        await message.channel.send(embed=embed)
        
    if message.content.startswith("-김수한무 개미"):
        embed=discord.Embed(title="개미작은", description="이것은 하양의 프로필 입니다.", color=0x00ff56)
        embed.set_author(name="개미", url="https://www.youtube.com/channel/UCFQtQICxAe5poesv_UmCEVA?app=desktop", icon_url="https://cdn.discordapp.com/attachments/716541654848503890/717286397840719882/externalFile_1.jpg")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/717016146716655677/717218639417442385/94ff9a0cbc761033.png")
        embed.add_field(name="이름", value="개미", inline=True)
        embed.add_field(name="주로 하는 말", value="ㅖㅣ!", inline=True)
        embed.add_field(name="좋아하는 게임", value="현:퉤롸뤼아", inline=True)
        embed.add_field(name="한마디.", value="ㅔ...", inline=True)
        embed.set_footer(text="이 사람은 하양 입니다.")
        await message.channel.send(embed=embed)
        
    if message.content.startswith("-김수한무 칠색조"):
        embed=discord.Embed(title="칠색조", description="이것은 칠색조의 프로필 입니다.", color=0x00ff56)
        embed.set_author(name="칠색조", url="https://www.youtube.com/channel/UClN0RrhhqXYLZlDDUNPH6Jg", icon_url="https://cdn.discordapp.com/attachments/714372925972545556/717289566574477373/unnamed.jpg")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/717016146716655677/717218639417442385/94ff9a0cbc761033.png")
        embed.add_field(name="이름", value="칠색조", inline=True)
        embed.add_field(name="주로 하는 말", value="ㅅ발", inline=True)
        embed.add_field(name="좋아하는 게임", value="테라리아", inline=True)
        embed.add_field(name="한마디.", value="ㄱㅊ나의영역임", inline=True)
        embed.set_footer(text="이 사람은 칠색조 입니다.")
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
