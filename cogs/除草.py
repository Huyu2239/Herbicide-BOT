import discord
from discord.ext import commands
import random

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
        for word in word_list:
            embed = discord.Embed(description=word)
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Grass(bot))