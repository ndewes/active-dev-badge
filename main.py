import os

import discord
from discord import app_commands
from discord.ext import commands

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

class ADB(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False

    async def on_ready(self):
        await tree.sync(guild=discord.Object(id=os.environ.get("GUILD")))
        self.synced = True
        print(f"Logged in as {self.user.name}")

bot = ADB()
tree = app_commands.CommandTree(bot)

@tree.command(
    name="activate",
    description="Activate your Badge",
    guild=discord.Object(id=os.environ.get("GUILD")),
)
async def self(interaction: discord.Interaction):
    await interaction.response.send_message(f"Your Badge are successfully reloaded.")

bot.run(os.environ.get("TOKEN"))
