import discord
from discord import app_commands
from discord.ext import commands

class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.help_message = """
```
Comandos:
!!ajuda - Mostra todos os comandos
!!play <keywords> - Procura a música e a toca via youtube
!!queue - mostra a queue atual
!!pular - pula a música atual
!!limpar - limpa a queue atual e para de tocar a música atual
!!sair - Desconecta do VC
!!pause - Toggle de pause da música
!!resume - Volta a tocar uma música pausada
```
"""

    @commands.command(name = "Ajuda", description = "Mostra os comandos do Bot")
    async def ajuda(self, ctx):
        await ctx.send(self.help_message)

async def setup(bot):
    await bot.add_cog(help(bot))