import discord
from discord.ext import commands
import os

# Crea los intents necesarios para que el bot pueda leer los mensajes
intents = discord.Intents.default()
intents.message_content = True  # Permite que el bot lea el contenido de los mensajes

# Crea la instancia del bot con el prefijo de comando
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.event
async def on_message(message):
    # Ignorar mensajes del propio bot
    if message.author == bot.user:
        return

    # Si el mensaje contiene "hola", responde
    if "hola" in message.content.lower():
        await message.channel.send(f"¡Hola {message.author.name}! ¿Cómo estás?")

    # Procesar comandos, si es que usas alguno
    await bot.process_commands(message)

# Carga el token desde una variable de entorno
token = os.getenv('DISCORD_TOKEN')  # Asegúrate de definir esta variable de entorno
bot.run(token)
