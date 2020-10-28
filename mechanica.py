from lib.helpers import get_config
from discord.ext import commands

import discord


config = get_config('./config.json')
bot = commands.Bot(command_prefix=config['prefix'])
extensions = ["extensions.manage", "extensions.shitpost", "extensions.members", "extensions.weather"]

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name} with ID {bot.user.id}")
    print('----------------------------------------------------------')


if __name__ == "__main__":
    for extension in extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f"{type(e).__name__}: {e}")
    
    bot.run(config["token"])