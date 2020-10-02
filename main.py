from discord.ext import commands
import os
import traceback
from dotenv import load_dotenv
load_dotenv()

INITIAL_EXTENSIONS = [
    "cogs.除草"
]

class MyBot(commands.Bot):
    def __init__(self, command_prefix):
        super().__init__(command_prefix)

        for cog in INITIAL_EXTENSIONS:
            try:
                self.load_extension(cog)
            except Exception:
                traceback.print_exc()

    async def on_ready(self):
        await self.change_presence(
            activity=discord.Game(
                name=f"{self.prefix}help | {len(self.guilds)}guilds"
            )
        )
        print('-----')
        print('起動')
        print('-----')

if __name__ == '__main__':
    bot = MyBot(command_prefix='ku!') 
    bot.run(os.environ['TOKEN'])
