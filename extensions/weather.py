from lib.helpers import error_handler
from discord.ext import commands, tasks
from datetime import datetime

import discord
import random

forecasts = [
    "It's going to be a sunny day",
    "It's going to be a rainy day",
    "It's going to be a windy day",
    "It's going to be a cloudy day",
]

class Weather(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

        self.send_forecast.start()


    @tasks.loop(hours=24)
    async def send_forecast(self):
        await self.channel.send(embed=discord.Embed(
            title=f"{datetime.date(datetime.now())}",
            description=random.choice(forecasts),
            color=discord.Colour.orange()
        ))

    @send_forecast.before_loop
    async def ready_up(self):
        await self.bot.wait_until_ready()
        self.channel = self.bot.get_channel(770672155318550528)
    

def setup(bot):
    bot.add_cog(Weather(bot))