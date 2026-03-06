import discord
import logging
from dotenv import load_dotenv
import os 
from discord.ext import commands
from db import get_connection

conn = get_connection()
cursor = conn.cursor()
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
    cursor.execute("""
    SELECT title, original_price, current_price, discount, img_src, game_src
    FROM game_sales ORDER BY discount DESC
    LIMIT 5
                   """)
    message = ""
    rows = cursor.fetchall()
    #another way to do it, (just practicing pandas lol)
    #df = pd.DataFrame(rows)
    #for index, row in df.iterrows():
        #message += f'{row[0]}, {row[1]}, {row[2]}, {row[3]}\n'
    for title, original, current, discount in rows:
        message += f'{title} | ${original} -> ${current}, {discount}% off\n'
    
    await ctx.send(embed=embed)

@bot.command(name='search')
async def search_game(ctx, *, query:str):
    game_to_search = f'%{query}%'
    cursor.execute(f"""
    SELECT * 
    FROM game_sales 
    WHERE title
    LIKE %s
    """,(game_to_search))
    row = cursor.fetchone()
    if row:
        embed = discord.Embed(
        title=f"{row[0]}",
        description=f"${row[1]} -> ${row[2]} | {row[3]}% off\n Source:{row[5]}",
        color=discord.Color.blue()
        )
        embed.set_image(url=row[4])
        await ctx.send(embed=embed)
    else:
        await ctx.send(f'No game in sale with title "{query}"')

bot.run(token, log_level=logging.INFO)
