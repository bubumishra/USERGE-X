#by @deleteduser420
import datetime
from userge import userge, Message

@userge.on_cmd("yearpb$", about={'header': "Year Progress Bar"})
async def year_elasped(message):
        
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
    
    string_out  = "<b>Year Progres</b>\n"
    string_out  += f"<code>{progress[num]} {percent}</code> `%`"
    await message.edit(string_out)