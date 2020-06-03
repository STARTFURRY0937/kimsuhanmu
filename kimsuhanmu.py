import discord
import openpyxl
import os
import datetime

client = discord.Client()
app = discord.Client()
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
    
    if message.content.startswith("-김수한무 내 정보"):
        date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
        embed = discord.Embed(color=0x00ff00)
        embed.add_field(name="이름", value=message.author.name, inline=True)
        embed.add_field(name="서버닉네임", value=message.author.display_name, inline=True)
        embed.add_field(name="가입날짜", value=str(date.year) + "년" + str(date.month) + "월" + str(date.day) + "일", inline=True)
        embed.add_field(name="아이디", value=message.author.id, inline=True)
        embed.set_thumbnail(url=message.author.avatar_url)
        await client.send_message(message.channel, embed=embed)
    
    if message.content.startswith("-김수한무야"):
        await message.channel.send("무슨 일 이십니까?")
    
    if message.content.startswith("-김수한무 바루호"):
        await message.channel.send("극비 사항 입니다.")
        
    if message.content.startswith("-김수한무 콩밤돌이"):
        await message.channel.send("극비 사항 입니다.")
        
        
    if message.content.startswith("-김수한무 네르"):
        embed=discord.Embed(title=".뉄", description="이것은 네르의 프로필 입니다.", color=0x00ff56)
        embed.set_author(name="네르", url="https://www.youtube.com/channel/UCf8xaoq1X55ZGnJn7kKtHwA", icon_url="https://cdn.discordapp.com/attachments/692941163920883732/717282429538140211/JPEG_20200103_190316.jpg")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/717016146716655677/717218639417442385/94ff9a0cbc761033.png")
        embed.add_field(name="이름", value="네르", inline=True)
        embed.add_field(name="주로 하는 말", value="ppap", inline=True)
        embed.add_field(name="좋아하는 게임", value="테라리아", inline=True)
        embed.add_field(name="한마디.", value="?", inline=True)
        embed.set_footer(text="이 사람은 네르 입니다.")
        await message.channel.send(embed=embed)
        
    if message.content.startswith("-김수한무 개미"):
        embed=discord.Embed(title="개미작은", description="이것은 개미의 프로필 입니다.", color=0x00ff56)
        embed.set_author(name="개미", url="https://www.youtube.com/channel/UCFQtQICxAe5poesv_UmCEVA?app=desktop", icon_url="https://cdn.discordapp.com/attachments/716541654848503890/717286397840719882/externalFile_1.jpg")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/717016146716655677/717218639417442385/94ff9a0cbc761033.png")
        embed.add_field(name="이름", value="개미", inline=True)
        embed.add_field(name="주로 하는 말", value="ㅖㅣ!", inline=True)
        embed.add_field(name="좋아하는 게임", value="현:퉤롸뤼아", inline=True)
        embed.add_field(name="한마디.", value="ㅔ...", inline=True)
        embed.set_footer(text="이 사람은 개미 입니다.")
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
        
    if message.content.startswith("-김수한무 콜리션"):
        embed=discord.Embed(title="콜리션", description="이것은 콜리션의 프로필 입니다.", color=0x00ff56)
        embed.set_author(name="콜리션", url="https://www.youtube.com/channel/UCek-VyGy6m_ux36a8YofH_A", icon_url="https://cdn.discordapp.com/attachments/716541654848503890/717292086990471198/1591086152394.jpg")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/717016146716655677/717218639417442385/94ff9a0cbc761033.png")
        embed.add_field(name="이름", value="콜리션", inline=True)
        embed.add_field(name="주로 하는 말", value="?", inline=True)
        embed.add_field(name="좋아하는 게임", value="테라리아", inline=True)
        embed.add_field(name="한마디.", value="(알고대답한거임)", inline=True)
        embed.set_footer(text="이 사람은 콜리션 입니다.")
        await message.channel.send(embed=embed)
        
    if message.content.startswith("-김수한무 약1한디아"):
        embed=discord.Embed(title="약한 디아Drunken DIA", description="이것은 약1한디아의 프로필 입니다.", color=0x00ff56)
        embed.set_author(name="약1한디아", url="https://www.youtube.com/channel/UCB_ON05OxGTBacY28B1EKWw?view_as=subscriber", icon_url="https://cdn.discordapp.com/attachments/716541654848503890/717294317932118086/unnamed_1.jpg")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/717016146716655677/717218639417442385/94ff9a0cbc761033.png")
        embed.add_field(name="이름", value="약1한디아", inline=True)
        embed.add_field(name="주로 하는 말", value="?", inline=True)
        embed.add_field(name="좋아하는 게임", value="테라리아", inline=True)
        embed.add_field(name="한마디.", value="약 필요하면 말하셈", inline=True)
        embed.set_footer(text="이 사람은 약1한디아 입니다.")
        await message.channel.send(embed=embed)
        
    if message.content.startswith("-김수한무 함수"):
        embed=discord.Embed(title="함수", description="이것은 함수의 프로필 입니다.", color=0x00ff56)
        embed.set_author(name="함수", url="https://www.youtube.com/channel/UCg3rWdTfpRlw_ZqcUuCOW2g/featured?view_as=subscriber", icon_url="https://cdn.discordapp.com/attachments/716541654848503890/717335317828599888/KakaoTalk_20200401_204511495_01.jpg")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/717016146716655677/717218639417442385/94ff9a0cbc761033.png")
        embed.add_field(name="이름", value="함수", inline=True)
        embed.add_field(name="주로 하는 말", value="?", inline=True)
        embed.add_field(name="좋아하는 게임", value="컴은 테라리아만 하는 함수", inline=True)
        embed.add_field(name="한마디.", value="쇼밤", inline=True)
        embed.set_footer(text="이 사람은 함수 입니다.")
        await message.channel.send(embed=embed)
        
    if message.content.startswith("-김수한무 ??"):
        embed=discord.Embed(title="??", description="이것은 ??의 프로필 입니다.", color=0x00ff56)
        embed.set_author(name="??", url="https://www.youtube.com/channel/UCjA53F_BR6Y8WRdE_Foh9rw?view_as=subscriber", icon_url="https://cdn.discordapp.com/attachments/716541654848503890/717336584084652120/unknown.png")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/717016146716655677/717218639417442385/94ff9a0cbc761033.png")
        embed.add_field(name="이름", value="??", inline=True)
        embed.add_field(name="주로 하는 말", value="?", inline=True)
        embed.add_field(name="좋아하는 게임", value="텔", inline=True)
        embed.add_field(name="한마디.", value="함변수태", inline=True)
        embed.set_footer(text="이 사람은 ?? 입니다.")
        await message.channel.send(embed=embed)
        
    if message.content.startswith("-김수한무 름표"):
        embed=discord.Embed(title="름표", description="이것은 름표의 프로필 입니다.", color=0x00ff56)
        embed.set_author(name="름표", url="https://www.youtube.com/channel/UCjA53F_BR6Y8WRdE_Foh9rw?view_as=subscriber", icon_url="https://cdn.discordapp.com/avatars/538589529263702017/b16422e6472d561f6a70b04680e7d300.webp?size=128")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/717016146716655677/717218639417442385/94ff9a0cbc761033.png")
        embed.add_field(name="이름", value="름표", inline=True)
        embed.add_field(name="주로 하는 말", value="흠터레스팅", inline=True)
        embed.add_field(name="특징", value="와 샌즈", inline=True)
        embed.add_field(name="한마디.", value="오늘 개학", inline=True)
        embed.set_footer(text="이 사람은 름표 입니다.")
        await message.channel.send(embed=embed)
        
    if message.content.startswith("ㅋㅋㅋ"):
        await message.channel.send("하하하하하 :)")
        
    if message.content.startswith("ㄷ"):
        await message.channel.send("후 덜덜덜...")

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
