import discord
import obswebsocket


if __name__ == "__main__":
    from bot import instance
    instance.load_extension('ext.cogs.obs_commands')
    instance.run()
