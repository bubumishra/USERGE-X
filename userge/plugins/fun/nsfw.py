import os
import urllib
import requests
from asyncio import sleep
from userge import userge , Message


@userge.on_cmd("boobs", about={
    'header': "Find some Bob",
    'usage': "{tr}boobs"})
async def boobs(message: Message):
    await message.edit("`Finding some big bobs 🧐...`")
    await asyncio.sleep(0.5)
    await message.edit("`Sending some big boobs 🌚...`")
    nsfw = requests.get('http://api.oboobs.ru/noise/1').json()[0]["preview"]
    pic_loc = "downloads/boobs.jpg"
    urllib.request.urlretrieve("http://media.oboobs.ru/{}".format(nsfw), pic_loc)
    await message.client.send_photo(message.chat.id, photo=pic_loc)
    os.remove(pic_loc)
    await message.delete()

@userge.on_cmd("butts", about={
    'header': "Find some Butts",
    'usage': "{tr}butts"})
async def butts(message: Message):
    await message.edit("`Finding some beautiful butts 🧐...`")
    await asyncio.sleep(0.5)
    await message.edit("`Sending some beautiful butts 🌚...`")
    nsfw = requests.get('http://api.obutts.ru/noise/1').json()[0]["preview"]
    pic_loc = "downloads/butts.jpg"
    urllib.request.urlretrieve("http://media.obutts.ru/{}".format(nsfw), pic_loc)
    await message.client.send_photo(message.chat.id, photo=pic_loc)
    os.remove(pic_loc)
    await message.delete()