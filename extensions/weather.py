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
        self.channel = bot.get_channel('770672155318550528')

        print(self.channel)

        self.send_forecast.start()


    @tasks.loop(seconds=10.0)
    async def send_forecast(self):
        await self.channel.send(embed=discord.Embed(
            title=f"{datetime.date(datetime.now())}",
            description=random.choice(forecasts),
            color=discord.Colour.orange()
        ))
    

def setup(bot):
    bot.add_cog(Weather(bot))