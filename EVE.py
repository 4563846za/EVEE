import discord
import os
from discord.ext import commands
import json
import asyncio
import yt_dlp
from myserver import server_on
import pandas as pd
import urllib.parse, urllib.request, re
from gtts import gTTS, lang
from discord.utils import get
from discord import FFmpegPCMAudio, Member, user

bot = commands.Bot(command_prefix='!',intents=discord.Intents.all())

eve_icon = 'https://media.discordapp.net/attachments/1012033549207076894/1242194388516601980/IMG_0398z.png?ex=664eed6d&is=664d9bed&hm=6a6c42bc54cba0418926c83ff4d3bdc1958a8355cae7655d0d8dad48091b27b2&=&format=webp&quality=lossless&width=701&height=701'
eve_iconf = 'https://media.discordapp.net/attachments/1012033549207076894/1240339785692745819/Untitled-1-Recovered.png?ex=664633f1&is=6644e271&hm=8b363d2e40c166d5793139a768fee49c42af52212ceffe5f74820fc222905658&=&format=webp&quality=lossless&width=701&height=701'
eve_image = 'https://media.discordapp.net/attachments/1012033549207076894/1237744870500728852/IMG_0397.png?ex=6645fdbd&is=6644ac3d&hm=6500a9bc2947e3764140481bc9f5d851421ac87f7ed3936af7de752376aedb2d&=&format=webp&quality=lossless&width=1079&height=701'
eve_images = 'https://media.discordapp.net/attachments/1012033549207076894/1242894958814433370/IMG_0500.png?ex=664f7fa2&is=664e2e22&hm=22b48fa5edd5a831350d04aedb12758cd3b316311982f1cfe3ebb6cdddedaa94&=&format=webp&quality=lossless&width=377&height=350'
eve_icons = 'https://media.discordapp.net/attachments/1012033549207076894/1242894958814433370/IMG_0500.png?ex=664f7fa2&is=664e2e22&hm=22b48fa5edd5a831350d04aedb12758cd3b316311982f1cfe3ebb6cdddedaa94&=&format=webp&quality=lossless&width=377&height=350'
eve_footer ='EVE Bot | อิฐอุ๋ง | Discord:@itoung | !help'

queues = {}
voice_clients = {}
youtube_base_url = 'https://www.youtube.com/'
youtube_results_url = youtube_base_url + 'results?'
youtube_watch_url = youtube_base_url + 'watch?v='
yt_dl_options = {"format": "bestaudio/best"}
ytdl = yt_dlp.YoutubeDL(yt_dl_options)
ffmpeg_options = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
                      'options': '-vn -filter:a "volume=0.25"'}

# //////////////////////////////////////////////////////////////////////////////////////////  BOT EVENT  ////////////////////////////////////////////////////////////////////////////////////////// #


@bot.event
async def on_ready():
    bgc = bot.get_channel
    eve = 1243546807254913096
    eda = 1154363890713505842
    yokai = 1241064234989780993
    online = [bgc(eve), bgc(eda), bgc(yokai)]
    text = f"EVE ตื่นแล้ว"
    emmbed = discord.Embed(title=text, color=0x66FFFF)

    emmbed.set_image(url=eve_images)
    emmbed.set_author(name=f"EVE", icon_url=eve_icon)
    emmbed.set_footer(text=eve_footer, icon_url=eve_iconf)

    for on in online:
        await on.send(embed=emmbed)

    await bot.change_presence(status=discord.Status,activity=discord.Activity(type=discord.ActivityType.watching,name="พวกมักมากในกามอยู่"))
    print('EVE ตื่นแล้ว')


@bot.event
async def on_member_join(member):
    ch = bot.get_channel 
    eve = 1243545770679074838
    holi = 1219232051895734326
    welcome = [ch(eve)]
    
    emmbed = discord.Embed(title='Hello Welcome! have room have condom',
                           description=f"ยินดีต้อนรับนะเจ้าบ้ากาม {member.mention}",
                           color=0x66FFFF,
                           timestamp=discord.utils.utcnow())

    emmbed.set_thumbnail(url=member.display_avatar)
    emmbed.set_image(url=eve_image)
    emmbed.set_author(name=f"EVE", icon_url=eve_icon)
    emmbed.set_footer(text=eve_footer, icon_url=eve_iconf)
    
    for wc in welcome:
        await wc.send(embed=emmbed)



@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(1243545770679074838)
    emmbed = discord.Embed(title=f"คนเงิ่ยนไปหายไปคนนึงแล้วล่ะ คราวนี้ที่นี่ก็น่าอยู่ขึ้นอีกนิด",
                          color=0x66FFFF,
                          timestamp=discord.utils.utcnow())

    emmbed.set_thumbnail(url=member.display_avatar)
    emmbed.set_image(url=eve_image)
    emmbed.set_author(name=f"EVE", icon_url=eve_icon)
    emmbed.set_footer(text=eve_footer, icon_url=eve_iconf)
    await channel.send(embed=emmbed)

# //////////////////////////////////////////////////////////////////////////////////////////  CHAT BOT  ////////////////////////////////////////////////////////////////////////////////////////// #

@bot.event
async def on_message(message):
    mes = message.content
    if mes == 'hi':
        await message.channel.send("hello")

    elif mes == '1':
        await message.channel.send("2")
    await bot.process_commands(message)

# //////////////////////////////////////////////////////////////////////////////////////////  Bot Command  ////////////////////////////////////////////////////////////////////////////////////////// #

bot.remove_command('help')

@bot.command()
async def help(ctx, user: discord.Member = None):
    if user is None:
        user = ctx.message.author

    inline = False
    emmbed = discord.Embed(title='ต้องการความช่วยเหลืออย่างงั้นหรอ', color=0x66FFFF)
    simple = {
        '```EVE Talking```': 'หากต้องการคุยกับ EVE ให้พิมข้อความที่ขึ้นต้นด้วย eve เช่น   **eveวันนี้สวยจังเลย**',
        '```EVE Speak```': 'หากต้องการให้ EVE พูดแทนให้ใช้ !eth(ภาษาไทย), !eth(ภาษาอังกฤษ) ตามด้วยคำเช่น   **!eth ปวดอึจังไปเข้าห้องน้ำแปปนะ**',
        ' ': ' ',
        '```EVE Command```': ' ',
        '!eve, !e': 'เรียก EVE ให้เข้ามาในแชทเสียงที่คุณอยู่ตอนนี้',
        '!leave, !l': 'เตะ EVE ออกจากแชทเสียง',
        '!profile, !pro': 'เรียกดูข้อมูลของคุณในเซิฟ หากต้องการดูข้อมูลคนอื่นให้เว้นวรรคแล้วแท็กชื่อ เช่น **!profile @Drengr, !pro @Drengr**',
        '!roll, !r': 'ทอยเต๋าโดยใส่จำนวนและชนิดของเต๋า และสามารถบวกหรือลบเลขหลังเต๋าได้ เช่น !r 1d20, !r 1d20+2',
        '!tarot, !taro, !tar, !t': 'สุ่มไพ่ทาโร้',
        '!leave, !l': 'เตะ EVE ออกจากแชทเสียง',
        ' ': ' ',
        '```EVE Music Command```': '',
        '!play, !p': 'เล่นเพลงให้พิม !p [ลิ้งค์เพลง,ชื่อเพลง],play [ลิ้งค์เพลง,ชื่อเพลง] **ใช้ได้ก็ต่อเมื่อไม่มีเพลงเล่นอยู่เท่านั้น**',
        '!pause, !pa': 'หยุดเพลงชั่วคราว',
        '!resume.!re': 'เล่นเพลงต่อจากที่หยุดไว้',
        '!skip, !s': 'ข้ามเพลงหรือบังคับให้เพลงจบ',
        '!queue, !q': 'เพิ่มเพลงลงในคิว หากต้องการเล่นเพลงในขณะที่เพลงยังเล่นอยู่ให้ใช้คำสั่งนี้แทน play',
        '!clear_q, !cl': 'ลบเพลงในคิวทั้งหมด',

    }
    for [fieldName, fieldVal] in simple.items():
        emmbed.add_field(name=fieldName, value=fieldVal, inline=inline)
    emmbed.set_thumbnail(url=user.display_avatar)
    emmbed.set_image(url=eve_image)
    emmbed.set_author(name=f"EVE", icon_url=eve_icon)
    emmbed.set_footer(text=eve_footer, icon_url=eve_iconf)

    await ctx.send(embed=emmbed)


# //////////////////////////////////////////////////////////////////////////////////////////  TTS  ////////////////////////////////////////////////////////////////////////////////////////// #

from googletrans import Translator

@bot.command(pass_context=True, aliases=['eth'])
async def eveth(ctx, *, text):
    language = 'th'
    output = gTTS(text=text, lang=language, slow=False, lang_check=True)
    output.save('voice.mp3')
    source = FFmpegPCMAudio('voice.mp3')
    player = ctx.guild.voice_client.play(source)

@bot.command(pass_context=True, aliases=['een'])
async def eveen(ctx, *, text):
    language = 'en'
    output = gTTS(text=text, lang=language, slow=False, lang_check=True)
    output.save('voice.mp3')
    source = FFmpegPCMAudio('voice.mp3')
    player = ctx.guild.voice_client.play(source)



def translate_text(text, dest_language='en'):
    translator = Translator()
    translation = translator.translate(text, dest=dest_language)
    return translation.text


@bot.command(pass_context=True, aliases=['th'])
async def translate(ctx, *, text, user: Member=None):
    if user is None:
        user = ctx.message.author

        tr = translate_text(text, dest_language='th')
        embed = discord.Embed(title="EVE Translator")
        embed.add_field(name="คำแปล",value=f"```{tr}```")
        embed.set_author(name=f"EVE", icon_url=eve_icon)
        embed.set_footer(text=eve_footer, icon_url=eve_iconf)
        embed.set_thumbnail(url=user.display_avatar)
        await ctx.send(embed=embed)

        language = 'th'
        output = gTTS(text=tr, lang=language, slow=False, lang_check=True)    
        output.save('voice.mp3')
        source = FFmpegPCMAudio('voice.mp3')
        player = ctx.guild.voice_client.play(source)




@bot.command(pass_context=True, aliases=['jp'])
async def translate_JP(ctx, *, text, user: Member=None):
    if user is None:
        user = ctx.message.author

        tr = translate_text(text, dest_language='ja')
        embed = discord.Embed(title="EVE Translator")
        embed.add_field(name="คำแปล",value=f"```{tr}```")
        embed.set_author(name=f"EVE", icon_url=eve_icon)
        embed.set_footer(text=eve_footer, icon_url=eve_iconf)
        embed.set_thumbnail(url=user.display_avatar)
        await ctx.send(embed=embed)

        language = 'ja'
        output = gTTS(text=tr, lang=language, slow=False, lang_check=True)    
        output.save('voice.mp3')
        source = FFmpegPCMAudio('voice.mp3')
        player = ctx.guild.voice_client.play(source)

# //////////////////////////////////////////////////////////////////////////////////////////  TTS  ////////////////////////////////////////////////////////////////////////////////////////// #



@bot.command(pass_context=True, aliases=['e'])
async def eve(ctx):
    file_path = 'EVE Hello.mp3'
    channel = ctx.author.voice.channel

    if not channel:
        return print('Invalid voice channel ID.')

    voice_client = await channel.connect()

    while True:
        voice_client.play(discord.FFmpegPCMAudio(file_path))
        await asyncio.sleep(voice_client.source.duration)
        voice_client.stop()



@bot.command(pass_context=True, aliases=['l'])
async def leave(ctx):
    channel = ctx.author.voice.channel
    voice_client = get(bot.voice_clients, guild=ctx.guild)

    if voice_client and voice_client.is_connected():
        await voice_client.disconnect()
        print(f'EVE ออกจากห้องเสียง{channel}แล้ว')
        await ctx.send('งั้นฉันไปละนะ')
    else:
        await ctx.send('EVE ออกจากห้องเสียง{channel}แล้ว | !help')


@bot.command(pass_context=True, aliases=['pro'])
async def profile(ctx, user: Member=None):

    if user is None:
        user = ctx.message.author

    inline = True
    emmbed = discord.Embed(title='ข้อมูลเบื้องต้นของ'f' {user.display_name}', color=0x66FFFF)
    userData = {
        'Name' : user.mention,
        'Role' : user.top_role,
        'Server' : user.guild,
        'Status': user.status
    }
    for [fieldName, fieldVal] in userData.items():
        emmbed.add_field(name=fieldName, value=fieldVal, inline=inline)
    emmbed.set_thumbnail(url=user.display_avatar)
    emmbed.set_image(url=user.display_avatar)
    emmbed.set_author(name=f"EVE", icon_url=eve_icon)
    emmbed.set_footer(text=eve_footer, icon_url=eve_iconf)

    await ctx.send(embed=emmbed)


@bot.command(pass_context=True, aliases=['k', 'ki'])
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)

@bot.command(pass_context=True, aliases=['ba'])
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)






# //////////////////////////////////////////////////////////////////////////////////////////  D&D  ////////////////////////////////////////////////////////////////////////////////////////// #

import random
import re   

@bot.command(name='update')
async def update(ctx, user: Member=None):

    if user is None:
        user = ctx.message.author

    inline = True
    emmbed = discord.Embed(title='ตัวละครของคุณได้เติบโตขึ้นแล้ว', color=0x66FFFF)
    userData = {
        'Player' : user.mention,
        'Clan' : user.top_role,
    }
    for [fieldName, fieldVal] in userData.items():
        emmbed.add_field(name=fieldName, value=fieldVal, inline=inline)
    emmbed.set_thumbnail(url=user.display_avatar)
    emmbed.set_image(url=eve_image)
    emmbed.set_author(name=f"EVE", icon_url=eve_icon)
    emmbed.set_footer(text=eve_footer, icon_url=eve_iconf)
    await ctx.send(embed=emmbed)



@bot.command(pass_context=True, aliases=['r'])
async def roll(ctx, dice: str):
    user: Member = None
    if user is None:
        user = ctx.message.author

    try:
        # ใช้ Regular Expression ในการแยกจำนวนเต๋า, หน้าเต๋า และแต้มบวก/ลบ
        match = re.match(r'(\d+)d(\d+)([+-]\d+)?', dice)
        if not match:
            raise ValueError('รูปแบบที่ใช้ไม่ถูกต้อง')

        fdice = int(match.group(1))
        bdice = int(match.group(2))
        modifier = int(match.group(3)) if match.group(3) else 0

        # ตรวจสอบเงื่อนไขขอบเขตของการทอยเต๋า
        if fdice > 0 and bdice > 0:
            rolls = [random.randint(1, bdice) for _ in range(fdice)]
            total = sum(rolls) + modifier
            result = ', '.join(map(str, rolls))
            crit = any(roll == bdice for roll in rolls)  # ตรวจสอบว่ามีการทอยได้ค่าสูงสุดหรือไม่
            crit_text = ' CRIT!!  โห ใหญ่มากๆ โคตรอูมเลย' if crit else ''
            modifier_text = f' {modifier:+}' if modifier != 0 else ''

            # สร้างข้อความผลลัพธ์ตามเงื่อนไข
            if modifier != 0:
                final_result = f'และได้: **{result}{modifier_text}{crit_text} รวมทั้งหมด {total}**'
            else:
                final_result = f'และได้: **{result}{crit_text}**'

            emmbed = discord.Embed(title=f'The Cause Dice', description=f'มีคนทอยเต๋าต้องสาป {bdice} หน้า')
            emmbed.add_field(name=f'{user.display_name} ได้ทำการทอยเต๋าแห่งชะตากรรม {bdice} หน้า', value=final_result)
            emmbed.set_thumbnail(url=user.display_avatar)
            emmbed.set_image(url='https://media4.giphy.com/media/oOBTO2UcSoaBJewZT0/200w.gif?cid=6c09b952aq8mj4ujgfjznfdpv3u2w0o994ylyvswuq2o1iaj&ep=v1_gifs_search&rid=200w.gif&ct=g')
            emmbed.set_author(name=f"Dice Roller!!", icon_url=eve_icon)
            emmbed.set_footer(text=eve_footer, icon_url=eve_iconf)
            await ctx.send(embed=emmbed)
        else:
            await ctx.send('กรุณาระบุจำนวนและหน้าของเต๋าเป็นตัวเลขบวก')

    except Exception as e:
        print(e)
        await ctx.send('รูปแบบที่ใช้ไม่ถูกต้อง กรุณาใช้รูปแบบตามดังนี้: !roll จำนวนเต๋าdหน้าเต๋า[+/-]แต้มที่เพิ่มเข้ามา')





# //////////////////////////////////////////////////////////////////////////////////////////  Music Command  ////////////////////////////////////////////////////////////////////////////////////////// #

@bot.event
async def play_next(ctx):
    if queues[ctx.guild.id] != []:
        url = queues[ctx.guild.id].pop(0)
        await play(ctx, url=url)


def format_duration(duration_seconds):
    minutes, seconds = divmod(duration_seconds, 60)
    hours, minutes = divmod(minutes, 60)
    if hours > 0:
        return f"{hours}:{minutes:02d}:{seconds:02d}"
    else:
        return f"{minutes}:{seconds:02d}"
    
    
@bot.command(pass_context=True, aliases=['p'])
async def play(ctx, *, url, user: Member=None):
    try:
        voice_client = await ctx.author.voice.channel.connect()
        voice_clients[voice_client.guild.id] = voice_client
    except Exception as e:
        print(e)

    try:

        if youtube_base_url not in url:
            query_string = urllib.parse.urlencode({
                'search_query': url
            })

            content = urllib.request.urlopen(
                youtube_results_url + query_string
            )

            search_results = re.findall(r'/watch\?v=(.{11})', content.read().decode())

            url = youtube_watch_url + search_results[0]

        loop = asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=False))

        song = data['url']
        player = discord.FFmpegOpusAudio(song, **ffmpeg_options)

        voice_clients[ctx.guild.id].play(player, after=lambda e: asyncio.run_coroutine_threadsafe(play_next(ctx),
                                                                                                  bot.loop))

        if user is None:
            user = ctx.message.author

        inline = False
        ydl = yt_dlp.YoutubeDL()
        info = ydl.extract_info(url, download=False)
        title = info.get('title', 'Unknown Title')
        im = info.get('thumbnail', '')
        duration = info.get('duration', 0)
        emmbed = discord.Embed(title=f'{title} ',description='เปิดเพลงให้แล้วน้าา'f' {user.mention}', color=0x66FFFF)
        userData = {
            'Duration':f'{format_duration(duration)}',
            'Link': url,
                    }
        for [fieldName, fieldVal] in userData.items():
            emmbed.set_author(name=f"เปิดเพลงแล้ว", icon_url=eve_icons)
            emmbed.add_field(name=fieldName, value=fieldVal, inline=inline)
        emmbed.set_thumbnail(url=user.display_avatar)
        emmbed.set_image(url=im)
        emmbed.set_footer(text=eve_footer, icon_url=eve_iconf)
        await ctx.send(embed=emmbed)

    except Exception as e:
        print(e)



@bot.command(pass_context=True, aliases=['cl'])
async def clear_q(ctx):
    if ctx.guild.id in queues:
        queues[ctx.guild.id].clear()
        await ctx.send("เคลียเพลงในคิวหมดแล้วน้าาา")
    else:
        await ctx.send("ไม่มีเพลงในคิวนะ จะให้เคลียอะไรอะ")

@bot.command(pass_context=True, aliases=['pa'])
async def pause(ctx):
    try:
        voice_clients[ctx.guild.id].pause()
    except Exception as e:
        print(e)

@bot.command(pass_context=True, aliases=['re'])
async def resume(ctx):
    try:
        voice_clients[ctx.guild.id].resume()
    except Exception as e:
        print(e)

@bot.command(name="stop")
async def stop(ctx):
    try:
        voice_clients[ctx.guild.id].stop()
        await voice_clients[ctx.guild.id].disconnect()
        del voice_clients[ctx.guild.id]
    except Exception as e:
        print(e)

@bot.command(pass_context=True, aliases=['q'])
async def queue(ctx, *, url, user: Member=None):
    if ctx.guild.id not in queues:
        queues[ctx.guild.id] = []
    queues[ctx.guild.id].append(url)
    if user is None:
        user = ctx.message.author

    inline = True
    emmbed = discord.Embed(description='เพิ่มเพลงเข้าคิวให้ละ'f' {user.mention}', color=0x66FFFF)
    userData = {
    }
    for [fieldName, fieldVal] in userData.items():
        emmbed.add_field(name=fieldName, value=fieldVal, inline=inline)
    emmbed.set_author(name=f"คิวเพลงแล้ว", icon_url=eve_icons)

    emmbed.set_thumbnail(url=user.display_avatar)
    emmbed.set_footer(text=eve_footer, icon_url=eve_iconf)

    await ctx.send(embed=emmbed)


@bot.command(pass_context=True, aliases=['s'])
async def skip(ctx, user: Member=None):
    voice_clients = get(bot.voice_clients, guild=ctx.guild)
    if user is None:
        user = ctx.message.author

    inline = True
    emmbed = discord.Embed(description='ข้ามเพลงให้แล้วน้าา'f' {user.mention}', color=0x66FFFF)
    userData = {
    }
    for [fieldName, fieldVal] in userData.items():
                emmbed.add_field(name=fieldName, value=fieldVal, inline=inline)
    emmbed.set_author(name=f"ข้ามเพลงแล้ว", icon_url=eve_icons)
    emmbed.set_thumbnail(url=user.display_avatar)
    emmbed.set_footer(text=eve_footer, icon_url=eve_iconf)

    await ctx.send(embed=emmbed)
    voice_clients.stop()



# ////////////////////////////////////////////////////////////////////////////////////////// Music Command  ////////////////////////////////////////////////////////////////////////////////////////// #



# Load tarot card data from JSON file
def load_tarot_cards():
    try:
        with open('tarot_cards.json', encoding='utf-8') as f:
            tarot_cards = json.load(f)
        return tarot_cards
    except FileNotFoundError:
        print("File 'tarot_cards.json' not found")
        return []
    except json.JSONDecodeError:
        print("File 'tarot_cards.json' is not properly formatted")
        return []

@bot.command(pass_context=True, aliases=['t', 'tar', 'taro'])
async def tarot(ctx, user: Member=None):
    tarot_cards = load_tarot_cards()
    if tarot_cards:
        card = random.choice(tarot_cards)
        if user is None:
            user = ctx.message.author
        inline = False
        embed = discord.Embed(title=card['name'], description=card['description'], color=0x00ff00)
        simple = {
            '**ความหมาย**' : '',
            'ความหมายในเชิงความรัก' : card['m1'],
            'หน้าที่การงาน' : card['m2'],
            'เรื่องการเงิน' : card['m3'],
            'เรื่องการเดินทาง': card['m4'],
            'เรื่องสุขภาพ': card['m5'],
            'ความหมายในเชิงแนะนำ': card['m6']
        }

        for [fieldName, fieldVal] in simple.items():
            embed.add_field(name=fieldName, value=fieldVal, inline=inline)
        embed.set_image(url=card['image'])
        embed.set_author(name=f"แม่หมอ อีฟ", icon_url=eve_icons)
        embed.set_thumbnail(url=user.display_avatar)
        embed.set_footer(text=eve_footer, icon_url=eve_iconf)
        await ctx.send(embed=embed)
    else:
        await ctx.send("Tarot card data is not available. Please check 'tarot_cards.json'.")


# //////////////////////////////////////////////////////////////////////////////////////////  Backjack  ////////////////////////////////////////////////////////////////////////////////////////// #

suits = ['♡', '♢', '♣', '♠']
ranks = [':two:', '3', ':four:', ':five:', ':six:', ':seven:', ':eight:', ':nine:', ':keycap_ten:', ':regional_indicator_j:', ':regional_indicator_q:', ':regional_indicator_k:', ':a:']
values = {':two:': 2, '3': 3, ':four:': 4, ':five:': 5, ':six:': 6, ':seven:': 7, ':eight:': 8, ':nine:': 9, ':keycap_ten:': 10, ':regional_indicator_j:': 10, ':regional_indicator_q:': 10, ':regional_indicator_k:': 10, ':a:': 11}

class Deck:
    def __init__(self):
        self.cards = [(rank, suit) for suit in suits for rank in ranks]
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        rank, suit = card
        self.value += values[rank]
        if rank == ':a:':
            self.aces += 1
        self.adjust_for_ace()

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

class BlackjackGame:
    def __init__(self):
        self.deck = Deck()
        self.player_hand = Hand()
        self.dealer_hand = Hand()

    def start_game(self):
        for _ in range(2):
            self.player_hand.add_card(self.deck.deal())
            self.dealer_hand.add_card(self.deck.deal())

    def hit(self, hand):
        hand.add_card(self.deck.deal())

    def get_hand_value(self, hand):
        return hand.value

    def display_hand(self, hand, hide_dealer_card=False):
        hand_display = []
        for idx, card in enumerate(hand.cards):
            if hide_dealer_card and idx == 0:
                hand_display.append("จั่ว")
            else:
                hand_display.append(f"{card[0]} {card[1]}")
        return "  ,  ".join(hand_display)

game = None

@bot.command()
async def blackjack(ctx):
    global game
    game = BlackjackGame()
    game.start_game()
    start =discord.Embed(title=f'เริ่มเล่นเกมแห่งความมืด Blackjack')
    player =discord.Embed(title=f'ไพ่บนมือของคุณ', description=f"{game.display_hand(game.player_hand)} = ``{game.get_hand_value(game.player_hand)}``", color=0x00ff00)
    player.set_footer(text='!blackjack, !hit, !stand', icon_url=eve_iconf)
    dealer =discord.Embed(title=f'มือเจ้า', description=f"{game.display_hand(game.dealer_hand)} = ``{game.get_hand_value(game.dealer_hand)}``", color=0x00ff00)
    await ctx.send(embed=start)    
    await ctx.send(embed=dealer)
    await ctx.send(embed=player)

@bot.command()
async def hit(ctx):
    global game
    if game:
        game.hit(game.player_hand)
        player = discord.Embed(title=f'ไพ่บนมือของคุณ', description=f"{game.display_hand(game.player_hand)} = ``{game.get_hand_value(game.player_hand)}``", color=0x00ff00)
        player.set_footer(text='!blackjack, !hit, !stand', icon_url=eve_iconf)        
        dealer = discord.Embed(title=f'เจ้ากินเรียบ ไม่นับไพ่ดีๆก็งี้แหละ', color=0x00ff00)
        dealer.set_footer(text='เริ่มใหม่กด !blackjack', icon_url=eve_iconf)
        dealer.set_image(url='https://cdn.discordapp.com/attachments/1253978000610033736/1253983438906720357/IMG_0500.png?ex=6677d695&is=66768515&hm=c64338f22a6146b7198f774dad8c8b4885ab3593fea57770065c7b5efb5e886c&')
        await ctx.send(embed=player)
        if game.get_hand_value(game.player_hand) > 21:
            await ctx.send(embed=dealer)
            game = None
    else:
        await ctx.send("เริ่มตาใหม่กด !blackjack")

@bot.command()
async def stand(ctx):
    global game
    if game:
        while game.get_hand_value(game.dealer_hand) < 17:
            game.hit(game.dealer_hand)
        dealer_value = game.get_hand_value(game.dealer_hand)
        player_value = game.get_hand_value(game.player_hand)
        dealer = discord.Embed(title=f'มือเจ้า', description=f"{game.display_hand(game.dealer_hand)} = ``{game.get_hand_value(game.dealer_hand)}``", color=0x00ff00)
        await ctx.send(embed=dealer)
        if dealer_value > 21 or player_value > dealer_value:
            win = discord.Embed(title=f'โกง โกงแน่ๆ แกโกงใช่มั้ย!!', color=0x00ff00)
            win.set_footer(text='เริ่มใหม่กด !blackjack', icon_url=eve_iconf)
            win.set_image(url='https://media.discordapp.net/attachments/1253978000610033736/1253982245652529253/IMG_0482.png?ex=6677d579&is=667683f9&hm=c55c6db96dc90694655753a8d31d77bd016c1cbafd289a70923538bdae9aff7d&=&format=webp&quality=lossless&width=684&height=700')
            await ctx.send(embed=win)
        elif player_value == dealer_value:
            draw = discord.Embed(title=f'ทำไพ่ปะเนี่ย', color=0x00ff00)
            draw.set_footer(text='เริ่มใหม่กด !blackjack', icon_url=eve_iconf)
            draw.set_image(url='https://media.discordapp.net/attachments/1253978000610033736/1253984540985131130/IMG_0484.png?ex=6677d79c&is=6676861c&hm=21628015e1b8d6070a7a6fe3be855b88e100f2d2e0200458c78581fee23c3946&=&format=webp&quality=lossless&width=686&height=701')
            await ctx.send(embed=draw)  
        else:
            lose = discord.Embed(title=f'ไปหัดมาใหม่นะ', color=0x00ff00)
            lose.set_footer(text='เริ่มใหม่กด !blackjack', icon_url=eve_iconf)
            lose.set_image(url='https://media.discordapp.net/attachments/1253978000610033736/1253983438906720357/IMG_0500.png?ex=6677d695&is=66768515&hm=c64338f22a6146b7198f774dad8c8b4885ab3593fea57770065c7b5efb5e886c&=&format=webp&quality=lossless&width=754&height=701')
            await ctx.send(embed=lose)    
        game = None
    else:
        await ctx.send("เริ่มตาใหม่กด !blackjack")
####################################################################################### Fobula Altima ######################################################################################## ชื่อไฟล์ JSON
data_file = 'char.json'

# ฟังก์ชันในการโหลดข้อมูลจาก JSON
def load_data():
    try:
        with open(data_file, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# ฟังก์ชันในการบันทึกข้อมูลลง JSON
def save_data(data):
    with open(data_file, 'w') as f:
        json.dump(data, f, indent=4)


character_data = {}

def initialize_character(user_id, sheet):
    # ตั้งค่าเริ่มต้นให้กับ character_data ของ user_id
    character_data[user_id] = {
        "name": sheet.iloc[5, 5],
        "image": sheet.iloc[23, 33] if sheet.iloc[23, 33] else "default_image_url.png",
        "fp": int(sheet.iloc[5, 31]),
        "level": int(sheet.iloc[5, 38]),
        "identity": sheet.iloc[6, 5],
        "origin": sheet.iloc[7, 19],
        "ep": int(sheet.iloc[7, 32]),
        "max_hp": int(sheet.iloc[10, 5]),
        "hp": int(sheet.iloc[12, 5]),
        "max_mp": int(sheet.iloc[14, 5]),
        "mp": int(sheet.iloc[14, 9]),
        "max_ip": int(sheet.iloc[16, 5]),
        "ip": int(sheet.iloc[16, 9]),
        "initiative_modifier": int(sheet.iloc[17, 9]),
        "defense": int(sheet.iloc[18, 9]),
        "md": int(sheet.iloc[19, 9]),
        "armor": sheet.iloc[21, 5],
        "mainhand": sheet.iloc[25, 5],
        "dex": sheet.iloc[9, 17],
        "ins": sheet.iloc[10, 17],
        "mig": sheet.iloc[11, 17],
        "wlp": sheet.iloc[12, 17],
        "zenit": sheet.iloc[39, 5]
    }


@bot.command(pass_context=True, aliases=['import'])
async def import_sheet(ctx, sheet_url: str):
    user_id = str(ctx.author.id)
    data = load_data()

    # แปลง URL ให้เป็นลิงก์ CSV
    csv_url = sheet_url.replace('/edit?usp=sharing', '/export?format=csv')

    # ตรวจสอบว่าผู้ใช้มีข้อมูลอยู่แล้วหรือไม่
    user_data = next((item for item in data if item["user_id"] == user_id), None)

    if user_data:
        # อัปเดตลิงก์ชีต
        user_data["character"] = csv_url  
        await ctx.send(f"{ctx.author.display_name} has updated the Google Sheets URL to: {csv_url}")
    else:
        # เพิ่มข้อมูลใหม่
        new_entry = {
            "user_id": user_id,
            "character": csv_url,
            "name": "sheet.iloc[5, 5]"  # เปลี่ยนเป็นฟังก์ชันหลังจากอ่านชีต
        }
        data.append(new_entry)
        await ctx.send(f"{ctx.author.display_name} has imported the Google Sheets URL: {csv_url}")

    save_data(data)

@bot.command()
async def char(ctx):
    user_id = str(ctx.author.id)
    data = load_data()

    # ค้นหาข้อมูลชื่อชีตของผู้ใช้
    user_data = next((item for item in data if item["user_id"] == user_id), None)

    if user_data:
        cheese_name = user_data["name"]
        sheet_url = user_data["character"]
        await ctx.send(f"{ctx.author.display_name}, your cheese is: {cheese_name} and the sheet URL is: {sheet_url}")
    else:
        await ctx.send(f"{ctx.author.display_name}, you haven't imported a sheet yet.")

def get_character_url(user_id):
    data = load_data()  # โหลดข้อมูลจาก JSON
    user_data = next((item for item in data if item["user_id"] == user_id), None)  # ค้นหาข้อมูลของผู้ใช้

    if user_data:
        return user_data.get("character")  # คืนค่าลิงก์ชีต
    else:
        return None  # ถ้าไม่พบข้อมูลของผู้ใช้



@bot.command()
async def all(ctx, user: discord.Member = None):
    if user is None:
        user = ctx.message.author

    user_id = str(user.id)
    sheet_url = get_character_url(user_id)

    if not sheet_url:
        await ctx.send(f"{user.display_name}, you haven't imported a sheet yet.")
        return

    sheet = pd.read_csv(sheet_url)

    # ตรวจสอบว่ามีข้อมูล character สำหรับ user_id นี้หรือยัง
    if user_id not in character_data:
        initialize_character(user_id, sheet)

    char_info = character_data[user_id]
    embed = discord.Embed(title=char_info["name"], color=0x66FFFF)

    # ดึงข้อมูลจาก dictionary มาแสดง
    embed.add_field(name="ชื่อ", value=char_info["name"], inline=True)
    embed.add_field(name="ตัวตน", value=char_info["identity"], inline=True)
    embed.add_field(name="แหล่งกำเนิด", value=char_info["origin"], inline=True)
    embed.add_field(name="Level", value=char_info["level"], inline=True)
    embed.add_field(name="Fabula Point", value=f'{char_info["fp"]}', inline=True)
    embed.add_field(name="Experience Points", value=f'{char_info["ep"]}', inline=True)
    embed.add_field(name="HP", value=f'{char_info["hp"]}/{char_info["max_hp"]}', inline=True)
    embed.add_field(name="MP", value=f'{char_info["mp"]}/{char_info["max_mp"]}', inline=True)
    embed.add_field(name="Inventory", value=f'{char_info["ip"]}/{char_info["max_ip"]}', inline=True)

    embed.set_thumbnail(url=user.display_avatar)
    embed.set_author(name=user.display_name, icon_url=user.display_avatar)
    embed.set_footer(text=eve_footer, icon_url=eve_iconf)
    embed.set_image(url=char_info["image"])

    await ctx.send(embed=embed)







@bot.command(pass_context=True, aliases=['g'])
async def game(ctx, *, text, user: discord.Member = None):
    if user is None:
        user = ctx.message.author
    
    user_id = str(user.id)
    sheet_url = get_character_url(user_id)
    
    if not sheet_url:
        await ctx.send(f"{user.display_name}, you haven't imported a sheet yet.")
        return
    
    # อ่านข้อมูลจาก CSV
    sheet = pd.read_csv(sheet_url)

    # เรียกฟังก์ชัน initialize_character เพื่อตั้งค่าเริ่มต้นหากยังไม่มีข้อมูล
    if user_id not in character_data:
        initialize_character(user_id, sheet)

    # ดึงข้อมูล character ของผู้ใช้
    char_info = character_data[user_id]

    # ตั้งค่าค่าสูงสุด
    max_hp = char_info["max_hp"]
    max_mp = char_info["max_mp"]
    max_ip = char_info["max_ip"]
    max_fp = 5  # ตามที่กำหนดในโค้ด

    # ตรวจสอบคำสั่งและจับคู่ตามค่า
    changes = {
        'hp': ('hp', max_hp, r'hp\s*([+-]?\d*)'),
        'mp': ('mp', max_mp, r'mp\s*([+-]?\d*)'),
        'ip': ('ip', max_ip, r'ip\s*([+-]?\d*)'),
        'ep': ('ep', None, r'ep\s*([+-]?\d*)'),
        'fp': ('fp', max_fp, r'fp\s*([+-]?\d*)')
    }

    updated_text = ""
    for key, (attr, max_value, pattern) in changes.items():
        match = re.match(pattern, text)
        if match:
            change = match.group(1)
            if change:
                # แปลง change เป็น int ก่อนบวก
                char_info[attr] += int(change)
                if max_value is not None:
                    char_info[attr] = max(0, min(char_info[attr], max_value))
            # อัปเดตค่าใน character_data เสมอ
            updated_text += f"**{key.upper()}**: {int(char_info[attr])}{'/' + str(max_value) if max_value else ''}\n"

    # สร้าง embed และส่งข้อความ
    embed = discord.Embed(title='Character Update', description=updated_text, color=0x66FFFF)
    embed.set_author(name=user.display_name, icon_url=user.display_avatar)
    embed.set_footer(text=eve_footer, icon_url=eve_iconf)
    embed.set_thumbnail(url=char_info["image"])  # ใช้ค่า image ที่กำหนดไว้ใน char_info
    await ctx.send(embed=embed)




#server_on()

bot.run("MTI0MDc1Mjc1MzUwOTQwNDc0Mg.Gmap4P.pKfzw33PjCBe9sApxpvPy6mQevFlAusRfygKjM")
