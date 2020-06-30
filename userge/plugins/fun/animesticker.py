import random
from asyncio import sleep
from random import choice

from userge import userge, Message


@userge.on_cmd("waifu", about={
'header': "Let your waifu say it for you UwU.",
'usage': "{tr}waifu [text or reply to msg]"})

async def waifu(message: Message):
    """ Creates random anime sticker! """

    text = message.input_or_reply_str
    if not text:
    	await message.edit("```You didn't gave the text so your Waifu ( ͡U ω ͡U ) ran away...```")
    	return
    animus = [20, 32, 33, 40, 41, 42, 58]
    sticcers = await userge.get_inline_bot_results(
    "stickerizerbot", f"#{random.choice(animus)}{text}")
    await userge.send_inline_bot_result(chat_id=message.chat.id,
    query_id=sticcers.query_id,
    result_id=sticcers.results[0].id)
