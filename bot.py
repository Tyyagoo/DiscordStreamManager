import discord
from discord.ext import commands
from obs import OBS

try:
    from settings import TOKEN, STREAMER_ID
except ImportError:
    print("Error on getting bot settings.\n"
          "Please verify settings.py file.")
    exit(0)


class DiscordBot(commands.Bot):

    def __init__(self, *args, **kwargs):
        super().__init__(command_prefix=['!', '.'], help_command=None, case_insensitive=True, *args, **kwargs)
        self.__TOKEN = TOKEN
        self.__STREAMER_ID = STREAMER_ID
        self.obs_ws = OBS()
        self.obs_ws.connect()
        self.target_voice_channel = None
        self.users_in_current_voice = 0
        self.block_changes = False

    @property
    def TOKEN(self) -> str:
        return self.__TOKEN

    @property
    def STREAMER_ID(self) -> int:
        return self.__STREAMER_ID

    def run(self) -> None:
        super().run(self.TOKEN)

    def on_ready(self) -> None:
        print(f"{self.user.name}#{self.user.discriminator} está online!")

    def update_stream_hud_state(self):
        if self.block_changes:
            return
        print(f"UPDATING STREAM HUD TO {self.users_in_current_voice}")
        self.obs_ws.change_scene_by_number(self.users_in_current_voice)

    async def on_voice_state_update(self, member: discord.Member, before: discord.VoiceState,
                                    after: discord.VoiceState):
        if before.channel == after.channel:
            # Ignore mute, deafen, video changes.
            return

        if member.id == STREAMER_ID:
            self.target_voice_channel = after.channel
            self.users_in_current_voice = 0

            if self.target_voice_channel is not None:
                for person in self.target_voice_channel.members:
                    self.users_in_current_voice += 1

            self.update_stream_hud_state()

        else:
            if self.target_voice_channel is not None:

                # Member connect
                if after.channel == self.target_voice_channel:
                    self.users_in_current_voice += 1

                # Member disconnect
                if before.channel == self.target_voice_channel:
                    self.users_in_current_voice -= 1

                self.update_stream_hud_state()

        print("DEBUG:")
        print(f"VoiceChannel: {self.target_voice_channel}")
        print(f"MemberCount: {self.users_in_current_voice}")


intents = discord.Intents.all()
instance = DiscordBot(intents=intents)
