from discord.ext import commands

class ChatCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print("Loaded ChatCommands cog")

def setup(bot):
    bot.add_cog(ChatCommands(bot))