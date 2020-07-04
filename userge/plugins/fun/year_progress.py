#by @deleteduser420
import datetime
from userge import userge
import math

@userge.on_cmd("yp$", about={'header': "Year Progress Bar"})
async def progresss(message):
    x = datetime.datetime.now()
    day = int(x.strftime("%j"))
    def truncate(number, digits) -> float:
        stepper = 10.0 ** digits
        return math.trunc(stepper * number) / stepper
    percent = truncate(( day / 365 * 100 ), 0)
    num = round(percent/5)
    
    progress = [
    "░░░░░░░░░░░░░░░░░░░░",
    "▓░░░░░░░░░░░░░░░░░░░",
    "▓▓░░░░░░░░░░░░░░░░░░",
    "▓▓▓░░░░░░░░░░░░░░░░░",
    "▓▓▓▓░░░░░░░░░░░░░░░░",
    "▓▓▓▓▓░░░░░░░░░░░░░░░",
    "▓▓▓▓▓▓░░░░░░░░░░░░░░",
    "▓▓▓▓▓▓▓░░░░░░░░░░░░░",
    "▓▓▓▓▓▓▓▓░░░░░░░░░░░░",
    "▓▓▓▓▓▓▓▓▓░░░░░░░░░░░",
    "▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░",
    "▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░",
    "▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░",
    "▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░",
    "▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░",
    "▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░",
    "▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░",
    "▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░",
    "▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░",
    "▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░",
    "▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓",
    ]

    message_out  =   "<b>Year Progress</b>\n"
    message_out  += f"<code>{progress[num]} {percent}</code>"
    message_out  +=  "`%`"
    await message.edit(message_out)
