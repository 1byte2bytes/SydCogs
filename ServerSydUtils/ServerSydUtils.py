import discord
from cogs.utils import checks
from discord.ext import commands
from .utils.dataIO import fileIO
from random import choice as randchoice
import os
import logging
import traceback
import aiohttp

log = logging.getLogger("ServerSydUtils")

class ServerSydUtils:

    """Insult Cog"""
    def __init__(self, bot):
        self.bot = bot
        self.session = aiohttp.ClientSession(loop=self.bot.loop)

    def __unload(self):
        self.session.close()

    @commands.command()
    @checks.is_co()
    async def setservicon(self, url):
        """Sets server icon"""
        try:
            async with self.session.get(url) as r:
                data = await r.read()
            server = self.bot.get_server("370628772489068565")
            await self.bot.edit_server(server, icon=data)
            await self.bot.say("Done.")
        except Exception as e:
            await self.bot.say(e)


def setup(bot):
    bot.add_cog(ServerSydUtils(bot))
