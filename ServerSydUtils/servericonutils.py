import discord
from discord.ext import commands
from .utils.dataIO import fileIO
from random import choice as randchoice
import os


class ServerSydUtils:

    """Insult Cog"""
    def __init__(self, bot):
        self.bot = bot

    @_set.command()
    @checks.is_co()
    async def setservicon(self, url):
        """Sets server icon"""
        try:
            async with self.session.get(url) as r:
                data = await r.read()
            await self.bot.edit_server(server=self.bot.get_server(370628772489068565), icon=data)
            await self.bot.say("Done.")
        except Exception as e:
            await self.bot.say("Error, check your console or logs for "
                               "more information.")
            log.exception(e)
            traceback.print_exc()


def setup(bot):
    bot.add_cog(Insult(bot))
