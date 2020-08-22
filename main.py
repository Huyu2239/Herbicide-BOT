from discord.ext import commands

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
        print('-----')
        print('起動')
        print('-----')

if __name__ == '__main__':
    bot = MyBot(command_prefix='!') 
    bot.run() 
