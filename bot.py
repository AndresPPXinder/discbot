"""
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
"""
"""
import discord
from discord.ext import commands
import os
from flask import Flask
import threading

# Crea los intents necesarios para que el bot pueda leer los mensajes
intents = discord.Intents.default()
intents.message_content = True  # Permite que el bot lea el contenido de los mensajes

# Crea la instancia del bot con el prefijo de comando
bot = commands.Bot(command_prefix="!", intents=intents)

# Crea un servidor Flask para hacer funcionar la URL pública
app = Flask(__name__)


@app.route('/')
def home():
    return "Bot está activo y funcionando"


def run_flask():
    app.run(host='0.0.0.0', port=80)


# Función para mantener el servidor Flask en un hilo separado
thread = threading.Thread(target=run_flask)
thread.start()


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
        await message.channel.send(f"¡Hola {message.author.name}! ¿Cómo estás?"
                                   )

    # Procesar comandos, si es que usas alguno
    await bot.process_commands(message)


# Carga el token desde una variable de entorno
token = os.getenv(
    'DISCORD_TOKEN')  # Asegúrate de definir esta variable de entorno

# Ejecuta el bot de Discord
bot.run(token)
"""

import discord
from discord.ext import commands
import os
from flask import Flask
import threading

# Crea los intents necesarios para que el bot pueda leer los mensajes
intents = discord.Intents.default()
intents.message_content = True  # Permite que el bot lea el contenido de los mensajes

# Crea la instancia del bot con el prefijo de comando
bot = commands.Bot(command_prefix="!", intents=intents)

# Crea un servidor Flask para hacer funcionar la URL pública
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot está activo y funcionando"

def run_flask():
    app.run(host='0.0.0.0', port=80)

# Función para mantener el servidor Flask en un hilo separado
thread = threading.Thread(target=run_flask)
thread.start()

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.event
async def on_message(message):
    # Ignorar mensajes del propio bot
    if message.author == bot.user:
        return

    # Diccionario con las categorías y sus respectivos personajes
    personajes = {
        "cuerpo a cuerpo": ["Rapunzel", "Peter", "Zeppetta", "Parfait", "Wukong", "Molly", "Duck", "Cisne"],
        "tirador": ["Hook", "Gumi", "Madame Lettuce", "Rambert", "Ovinus", "Flare", "Robin", "Habelin"],
        "ataque en área": ["Ravi", "Aoi", "Jacko", "Nui", "Victor", "Pinocchio", "Proc"],
        "asesino": ["Kurenai", "Wolfgang", "Red", "Master Cat", "Snow", "Ali", "Woochi", "Javert"],
        "estratega": ["Goldie", "Loren and Vex", "Octavia", "Alice", "Brick", "Witch Queen", "Narsha", "Briar"],
        "protector": ["Kaiser", "Marina", "Timun", "Don Quijote", "Cindy", "Yong Yong", "Maya"]
    }

    # Comprobamos si el mensaje contiene alguna de las categorías
    for categoria, lista in personajes.items():
        if categoria in message.content.lower():
            await message.channel.send(f"**Personajes de {categoria}:** {', '.join(lista)}")
            return  # Evitamos que el bot siga buscando otras categorías

    # Procesar comandos si es que usas alguno
    await bot.process_commands(message)

# Carga el token desde una variable de entorno
token = os.getenv('DISCORD_TOKEN')  # Asegúrate de definir esta variable de entorno

# Ejecuta el bot de Discord
bot.run(token)
