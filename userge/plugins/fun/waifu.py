""" Creates random anime girl sticker """
import random
from userge import userge, Message

@userge.on_cmd("waifu", about={
    'header': "Say it with cute anime girl sticker",
    'usage': "{tr}waifu [text | reply to message]",
    'example': "{tr}waifu Onii-chan"})
async def waifu(message: Message):
    """ Creates random anime girl sticker! """

    text = message.input_or_reply_str
    if not text:
        await message.edit("```You didn't gave the text so your Waifu ( ͡U ω ͡U ) ran away...```", del_in=3)
        return
    try:
        animus = [20, 32, 33, 40, 41, 42, 58]
        stickers = await userge.get_inline_bot_results(
            "stickerizerbot",
            f"#{random.choice(animus)}{text}"
        )
        await userge.send_inline_bot_result(
            chat_id=message.chat.id,
            query_id=stickers.query_id,
            result_id=stickers.results[0].id
        )
        await message.delete()
    except IndexError:
        await message.edit("```List index out of range```", del_in=3)
    
    
