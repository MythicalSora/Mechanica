from lib.helpers import error_handler
from discord.ext import commands

import discord

class Shitpost(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


def setup(bot):
    bot.add_cog(Shitpost(bot))