import discord
import os

from datetime import datetime, time
from discord.ext import tasks
from dotenv import load_dotenv
from eventhelpers import act_on_sheet_for_day
from zoneinfo import ZoneInfo

load_dotenv()
bot = discord.Bot()

t = time(13, tzinfo=ZoneInfo('America/New_York'))

@bot.event
async def on_ready():
    print(f"{bot.user} connected.")
    send_message.start()


@tasks.loop(time=t)
async def send_message():
    print("Running at " + str(datetime.now().time()))
    u = await bot.fetch_user(677683613277487121)
    channel = await bot.create_dm(u)

    today = datetime.strptime('3/30/2027', "%m/%d/%Y")
    # today = datetime.now()

    await act_on_sheet_for_day(today, lambda e: channel.send(e.to_message(today)))

bot.run(str(os.getenv("TOKEN")))
