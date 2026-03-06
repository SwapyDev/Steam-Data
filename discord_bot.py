import discord
import logging
from dotenv import load_dotenv
import os 
from discord.ext import commands
from db import get_connection


load_dotenv()
token = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    logging.info(f'Logged in as {bot.user}')

@bot.command(name='offers')
async def offers_command(ctx):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    SELECT title, original_price, current_price, discount
    FROM game_sales ORDER BY discount DESC
    LIMIT 5
                   """)
    message = ""
    rows = cursor.fetchall()
    #another way to do it, (just practicing pandas lol)
    #df = pd.DataFrame(rows)
    #for index, row in df.iterrows():
        #message += f'{row[0]}, {row[1]}, {row[2]}, {row[3]}\n'
    for row in rows:
        message += f'{row[0]}, {row[1]}, {row[2]}, {row[3]}\n'
    
    await ctx.send(message)

bot.run(token, log_level=logging.INFO)
