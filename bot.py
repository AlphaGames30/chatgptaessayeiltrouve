import os
import json
import discord
from discord.ext import commands
from discord import app_commands
from flask import Flask

# ---------- Flask part ----------
app = Flask(__name__)

@app.route("/")
def home():
    return "Bot Discord Global Chat actif 🚀"

# ---------- Discord bot part ----------
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Fichier pour stocker les salons synchronisés
SYNC_FILE = "synced_channels.json"

def load_channels():
    if os.path.exists(SYNC_FILE):
        with open(SYNC_FILE, "r") as f:
            return json.load(f)
    return []

def save_channels(channels):
    with open(SYNC_FILE, "w") as f:
        json.dump(channels, f)

# Commandes slash
@bot.tree.command(name="addsync", description="Ajoute ce salon au chat global")
async def addsync(interaction: discord.Interaction):
    channels = load_channels()
    if interaction.channel.id not in channels:
        channels.append(interaction.channel.id)
        save_channels(channels)
        await interaction.response.send_message("✅ Ce salon est ajouté au chat global.", ephemeral=True)
    else:
        await interaction.response.send_message("⚠️ Ce salon est déjà synchronisé.", ephemeral=True)

@bot.tree.command(name="removesync", description="Retire ce salon du chat global")
async def removesync(interaction: discord.Interaction):
    channels = load_channels()
    if interaction.channel.id in channels:
        channels.remove(interaction.channel.id)
        save_channels(channels)
        await interaction.response.send_message("❌ Ce salon a été retiré du chat global.", ephemeral=True)
    else:
        await interaction.response.send_message("⚠️ Ce salon n'était pas synchronisé.", ephemeral=True)

# Relai des messages
@bot.event
async def on_message(message):
    if message.author.bot:
        return

    channels = load_channels()
    if message.channel.id in channels:
        for cid in channels:
            if cid != message.channel.id:
                channel = bot.get_channel(cid)
                if channel:
                    await channel.send(f"**{message.author.display_name}** : {message.content}")

# Lancement
if __name__ == "__main__":
    # Récupère le token depuis les variables d'environnement
    TOKEN = os.getenv("DISCORD_TOKEN")

    import threading
    def run_flask():
        app.run(host="0.0.0.0", port=8080)

    threading.Thread(target=run_flask).start()
    bot.run(TOKEN)
