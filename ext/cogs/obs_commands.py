import discord
from discord.ext import commands

try:
    from settings import SPONSORS
except ImportError:
    print("Erro ao importar lista de patrocinadores.")
    print("Caso você não deseje usar essa função, defina:")
    print("SPONSORS = {}")


class ObsCommands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["ad", "anuncio"])
    @commands.has_permissions(administrator=True)
    async def _ad(self, ctx: commands.Context, sponsor: str = None):
        if sponsor is None:
            self.bot.block_changes = False if self.bot.block_changes else True
            true_msg = "Agora o bot **NÃO** pode alterar as cenas."
            false_msg = "Agora o bot **PODE** alterar as cenas."
            await ctx.channel.send(true_msg if self.bot.block_changes else false_msg)

            # Force stream hud update.
            if self.bot.block_changes is False:
                self.bot.update_stream_hud_state()

        else:
            lowercased_sponsors_keys = [sponsor_name.lower() for sponsor_name in SPONSORS.keys()]
            print(lowercased_sponsors_keys)
            if sponsor.lower() in lowercased_sponsors_keys:
                self.bot.block_changes = True
                for sp in SPONSORS.keys():
                    if sp.lower() == sponsor.lower():
                        print(SPONSORS[sp])
                        self.bot.obs_ws.change_scene(SPONSORS[sp])
                        await ctx.channel.send(f"Passando o anúncio da: **{sponsor.upper()}**,(CENA: {SPONSORS[sp]})")
                        break

            else:
                await ctx.channel.send(f"Esse anunciante não existe: **{sponsor.lower()}**")

    @commands.command(aliases=["fu", "update", "forceupdate"])
    @commands.has_permissions(administrator=True)
    async def _force_update(self, ctx: commands.Context):
        self.bot.update_stream_hud_state()
        await ctx.reply("O HUD foi atualizado.")

    @_ad.error
    async def _ad_error(self, ctx: commands.Context, error):
        await ctx.reply("Esse comando é restrito aos administradores do servidor.")

    @_force_update.error
    async def _force_update_error(self, ctx: commands.Context, error):
        await ctx.reply("Esse comando é restrito aos administradores do servidor.")


def setup(bot):
    bot.add_cog(ObsCommands(bot))
