import asyncio, websockets
from discord.ext import commands

class ChatCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print("Loaded ChatCommands cog")
    
    @commands.command()
    async def ping(self, ctx):
        await ctx.send("pong")


def setup(bot):
    bot.add_cog(ChatCommands(bot))