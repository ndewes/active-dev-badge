import os
import datetime

import discord
from discord import app_commands
from discord.ext import commands

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())
token = os.environ.get('TOKEN')
guild_id = os.environ.get('GUILD')

class ADB(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False

    async def on_ready(self):
        await tree.sync(guild=discord.Object(id=guild_id))
        self.synced = True
        print(f'Logged in as {self.user.name}')

bot = ADB()
tree = app_commands.CommandTree(bot)

@tree.command(
    name='activate',
    description='Activate your Badge',
    guild=discord.Object(id=guild_id),
)
async def self(interaction: discord.Interaction):
    await interaction.response.send_message('Your Badge are successfully **activated**.')
    today = datetime.datetime.today()
    next_activate = (today + datetime.timedelta(days=30)).strftime('%d.%m.%Y %H:%M')
    await interaction.channel.send(f'Next activate on **{next_activate}**')

bot.run(token=token)
