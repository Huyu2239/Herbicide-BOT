import discord
from discord.ext import commands
import random
import asyncio

grass_list = [
    "www",
    "ｗｗｗ",
    "草w",
    "草ｗ"
]
word_list = [
    """
‪　　　∧,,∧
　 (；`・ω・）　　,
　 /　ｏ={=}ｏ , ', ´
､､しー-Ｊミ(.@)ｗｗｗｗｗｗｗｗｗｗｗ
    """,
    """
‪　　　　_, ._
　　（　・ω・）んも～
　　○=｛=｝〇,
　 　|:::::::::＼, ', ´
､､､､し ､､､((（.＠）ｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗ
    """,
    """
　　 　 　 _, ,_
　ｗ　　（・ω・　）
　(~)､ /　　　i　 ）
　 ＼ `　|＿/　/|
　　 `ー_（　__ノ　|
　　　 （　 `（　 ､ﾉ
ｗｗｗｗｗ_ﾉ`i__ﾉ
    """,
    """

　　　, ; .'´　｀. ﾞ ;　｀
　　　,.'.;´," :´,´'　. ﾞ　.｀　.
　　　,.'.;´," :.　　　　　　 ､ヘ＿__
　　　　　　　　　　　　　　|　＿　|
　　　.,,.,.,,,.,.,,,.,.,,,.,.,,,.,.,,,.,,,.,.,◎　◎ｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗ
    """,
    """
草刈り(;゜(エ)゜)o >━━"((卍))"ﾌﾞﾝﾌﾞﾝ♪
    """,
    """
草刈り～(o⌒▽⌒)o>━━"((卍))"ﾌﾞﾝﾌﾞﾝ♪
    """,
    """
草刈り(o･∀･ )o>――"((χ))"ﾌﾞﾝﾌﾞﾝ♪
    """,
    """
ｗｗWｗｗｗｗｗｗ､',,',､',,',WｗｗｗWｗｗWｗｗWｗｗ
    """,
    """
ｗｗWｗｗｗｗｗｗ､',,',､',,',WｗｗｗWｗｗWｗｗWｗｗ
ｗｗｗｗ､',､'',,',､',,',,､',,､',,',,､､',ｗWｗｗWｗｗｗWｗ
,,,,,,,､',､､','､',､',,',,,､',,',,,､',,',,､ミ ,､,'ミｗミｗｗｗｗｗｗWｗ
､',､',,,､',',､',,,,,,,,,,,,,,,,,,,,,彡,,＼,',ヽ,,|ゝ, ',ｗﾐｗWｗｗｗｗｗ
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,（（,,',,､',ヽ,,）ﾉ,',／ゝ））ｗWｗｗｗ
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,, ',／⌒(ﾟдﾟ)ノ─,',ｗｗｗｗWｗｗ
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,（（､',',/,､',（,､',,ヽ､',´ﾉﾉWｗｗｗｗｗ
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,ミ､/､', ',,_|,, ',,,,,,＼彡ｗｗｗWｗｗｗｗ
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,彡,,｀彡ｗｗWｗｗｗWｗｗ
ｗｗｗWｗｗｗWｗｗｗｗWｗｗｗｗｗWｗｗｗWｗｗｗ
WｗｗｗWｗWｗｗｗWｗｗｗｗｗWｗｗｗｗWｗｗｗWｗｗ
    """
]

class Grass(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener() 
    async def on_message(self, message):
        if message.author.bot: return
        msg = ''.join(random.choice(word_list,))
        for grass in grass_list:
            if grass in message.content and 'http' not in message.content:
                await message.channel.send(msg)
                break
        return
    
    @commands.command()
    async def grass(self, ctx):
        grass = '\n'.join(grass_list)
        embed = discord.Embed(title="反応する単語", description=grass)
        await ctx.send(embed=embed)

    @commands.command()
    async def words(self, ctx):
        page = 0
        msg = await ctx.send('読み込み中・・・')
        react_list = [
            "\N{BLACK LEFT-POINTING TRIANGLE}",  # 戻る
            "\N{BLACK RIGHT-POINTING TRIANGLE}",  # 進む
            "\N{BLACK SQUARE FOR STOP}\N{VARIATION SELECTOR-16}"#終了
        ]
        for react in react_list:
            await msg.add_reaction(react)
        embed = discord.Embed(description = word_list[page])
        await msg.edit(content=f'[{page + 1}/{len(word_list)}]',embed=embed)
        def check(reaction, user):
            if reaction.message.id != msg.id or ctx.author.bot or user != ctx.author:
                return False
            elif str(reaction.emoji) in react_list:
                return reaction, user
        while not self.bot.is_closed():
            try:
                react, user= await self.bot.wait_for("reaction_add", check=check, timeout=300)
            except asyncio.TimeoutError:
                await msg.delete()
                await ctx.message.delete()
                break
            emoji = str(react.emoji)
            await msg.remove_reaction(emoji, user)
            if emoji in react_list:
                if emoji == "\N{BLACK LEFT-POINTING TRIANGLE}" and page != 0:
                    page = page - 1 
                if emoji == "\N{BLACK RIGHT-POINTING TRIANGLE}" and page != len(word_list)-1:
                    page = page + 1
                if emoji == "\N{BLACK SQUARE FOR STOP}\N{VARIATION SELECTOR-16}":
                    await msg.delete()
                    await ctx.message.delete()
                    break
            embed = discord.Embed(description = word_list[page])
            await msg.edit(content=f'[{page + 1}/{len(word_list)}]',embed=embed)


def setup(bot):
    bot.add_cog(Grass(bot))