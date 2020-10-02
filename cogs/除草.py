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
草刈り～(o⌒▽⌒)o>━━"((卍))"ﾌﾞﾝﾌﾞﾝ♪
    """,
    """
草刈り(o･∀･ )o>――"((χ))"ﾌﾞﾝﾌﾞﾝ♪
    """,
    """
ｗｗWｗｗｗｗｗｗ､',,',､',,',WｗｗｗWｗｗWｗｗWｗｗ
    """,
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
　　　　｡ﾟ･.ｗﾐﾐﾐｯ
んもー ｗ (ﾚ)ﾐﾐｗﾐ
　　_,._　//ｗ/""
　( ･ω･)// 川､｡､､､､
　/ ＿l]つwｗﾐｗﾐｗﾐ
｛{]⌒))ﾐｗﾐｗｗｗﾐ"
　/しｲ| ヾ＼川／
`//==||ｉヾ巛ｲ ､､､｡
//===||ｗ　|||ﾐｗﾐﾐ
/====||　｡ﾐﾐﾐ|//""
=====|| ﾐｗｗ//
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
            if grass in message.content:
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
                await ctx.message.clear_reactions()
                break
            emoji = str(react.emoji)
            await msg.remove_reaction(emoji, user)
            if emoji in react_list:
                if emoji == "\N{BLACK LEFT-POINTING TRIANGLE}" and page != 0:
                    page = page - 1 
                if emoji == "\N{BLACK RIGHT-POINTING TRIANGLE}" and page != len(word_list):
                    page = page + 1
                if emoji == "\N{BLACK SQUARE FOR STOP}\N{VARIATION SELECTOR-16}":
                    await msg.delete()
                    await ctx.message.delete()
                    break
            embed = discord.Embed(description = word_list[page])
            await msg.edit(content=f'[{page + 1}/{len(word_list)}]',embed=embed)


def setup(bot):
    bot.add_cog(Grass(bot))