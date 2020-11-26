from lib.helpers import is_developer, error_handler, notif_handler, no_developer
from discord.ext import commands

import discord

class Manage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    

    @commands.command()
    async def load(self, ctx, extension):
        if is_developer(ctx.message.author):
            try:
                self.bot.load_extension(extension)
                await ctx.send(embed=notif_handler(f"Extension '{extension}' successfully loaded!"))
            except Exception as e:
                await ctx.send(embed=error_handler(e))
        else:
            await ctx.send(embed=no_developer())
    

    @commands.command()
    async def unload(self, ctx, extension):
        if is_developer(ctx.message.author):
            self.bot.unload_extension(extension)
            await ctx.send(embed=notif_handler(f"Extension '{extension}' successfully unloaded!"))
        else:
            await ctx.send(embed=no_developer())
    

    @commands.command()
    async def reload(self, ctx, extension):
        if is_developer(ctx.message.author):
            self.bot.unload_extension(extension)

            try:
                self.bot.load_extension(extension)
                await ctx.send(embed=notif_handler(f"Extension '{extension} succesfully reloaded!'"))
            except Exception as e:
                await ctx.send(embed=error_handler(e))
        else:
            await ctx.send(embed=no_developer())


def setup(bot):
    bot.add_cog(Manage(bot))