import discord
import os

from datetime import datetime
from discord.ext import tasks
from dotenv import load_dotenv
from eventhelpers import act_on_sheet_for_day

load_dotenv()
bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"{bot.user} connected.")


@tasks.loop(minutes=15)
async def send_message():
    print("Running at" + str(datetime.now().time()))
    u = await bot.fetch_user(677683613277487121)
    channel = await bot.create_dm(u)

    today = datetime.strptime('3/30/2027', "%m/%d/%Y")
    # today = datetime.now()

    act_on_sheet_for_day(today, lambda e: channel.send(e.to_message(today)))

bot.run(str(os.getenv("TOKEN")))
