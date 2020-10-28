from lib.helpers import error_handler, permission_error, notif_handler
from discord.ext import commands

import discord

class Members(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def approve(self, ctx, target: discord.Member):
        await target.add_roles(discord.utils.get(target.guild.roles, name='Approved'))
        await target.remove_roles(discord.utils.get(target.guild.roles, name='Unapproved'))

        await ctx.send(embed=discord.Embed(
            title=f"Approved {target.display_name}!",
            color=discord.Colour.green()
        ))


    @approve.error
    async def approve_error(self, error, ctx):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(embed=error_handler('manage_roles'))


def setup(bot):
    bot.add_cog(Members(bot))