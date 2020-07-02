#by @deleteduser420
import datetime
from userge import userge

@userge.on_cmd("yearpb$", about={'header': "Year Progress Bar"})
async def progresss(message):
    x = datetime.datetime.now()
    day = int(x.strftime("%j"))
    percent = round( day / 365 * 100 )
    num = round(percent/5)
    
    progress = [
    "░░░░░░░░░░░░░░░░░░░",
    "▓░░░░░░░░░░░░░░░░░░",
    "▓▓░░░░░░░░░░░░░░░░░",
    "▓▓▓░░░░░░░░░░░░░░░░",
    "▓▓▓▓░░░░░░░░░░░░░░░",
    "▓▓▓▓▓░░░░░░░░░░░░░░",
    "▓▓▓▓▓▓░░░░░░░░░░░░░",
    "▓▓▓▓▓▓▓░░░░░░░░░░░░",
    "▓▓▓▓▓▓▓▓░░░░░░░░░░░",
    "▓▓▓▓▓▓▓▓▓░░░░░░░░░░",
    "▓▓▓▓▓▓▓▓▓▓░░░░░░░░░",
    "▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░",
    "▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░",
    "▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░",
    "▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░",
    "▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░",
    "▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░",
    "▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░",
    "▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░",
    "▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓",
    ]
    message_out  =   "<b>Year Progress</b>\n"
    message_out  += f"<code>{progress[num]} {percent}</code>"
    message_out  +=  "`%`"
    await message.edit(message_out)