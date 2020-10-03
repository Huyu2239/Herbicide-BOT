import discord
from discord.ext import commands
class Status(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    async def status_change(self):
        await self.bot.change_presence(
            activity=discord.Game(
                name=f"ku!help | {len(self.bot.guilds)}guilds"
            )
        )

    @commands.Cog.listener() 
    async def on_guild_join(self, guild):
        await self.status_change()

    @commands.Cog.listener() 
    async def on_guild_remove(self, guild):
        await self.status_change()

def setup(bot):
    bot.add_cog(Status(bot))