#ported for Userge-X by @DeletedUser420
import os
import json
import aiohttp
import asyncio
from asyncio import sleep
from userge import userge, Message
import random
from jikanpy import Jikan
from jikanpy.exceptions import APIException
from urllib.parse import quote as urlencode

jikan = Jikan()
@userge.on_cmd("anime", about={
    'header': "Get details about given anime",
    'usage': "{tr}anime [text | reply to message]",
    'example': "{tr}anime naruto"})

async def anim_(message: Message):
    """ For Finding anime info """
    msg = message.input_or_reply_str
    res = ""
    if not msg:
        await message.edit("```You didn't even gave the text and you call youself Otaku? (⩾﹏⩽)...```", del_in=3)
        return
    
    try:
        res = jikan.search("anime", msg)
    except APIException:
        await message.edit("Error connecting to the API. Please try again!")
        return ""
    try:
        res = res.get("results")[0].get("mal_id") # Grab first result
    
    except APIException:
        await message.edit("Error connecting to the API. Please try again!")
        return ""
    if res:
        anime = jikan.anime(res)
        title = anime.get("title")
        japanese = anime.get("title_japanese")
        type = anime.get("type")
        duration = anime.get("duration")
        synopsis = anime.get("synopsis")
        source = anime.get("source")
        status = anime.get("status")
        episodes = anime.get("episodes")
        score = anime.get("score")
        rating = anime.get("rating")
        genre_lst = anime.get("genres")
        genres = ""
        for genre in genre_lst:
            genres += genre.get("name") + ", "
        genres = genres[:-2]
        studios = ""
        studio_lst = anime.get("studios")
        for studio in studio_lst:
            studios += studio.get("name") + ", "
        studios = studios[:-2]
        duration = anime.get("duration")
        premiered = anime.get("premiered")
        image_url = anime.get("image_url")
        url = anime.get("url")
        trailer = anime.get("trailer_url")
    else:
        await message.edit("No results found!")
        return
    rep = f"<b>{title} ({japanese})</b>\n"
    rep += f"<b>Type:</b> <code>{type}</code>\n"
    rep += f"<b>Source:</b> <code>{source}</code>\n"
    rep += f"<b>Status:</b> <code>{status}</code>\n"
    rep += f"<b>Genres:</b> <code>{genres}</code>\n"
    rep += f"<b>Episodes:</b> <code>{episodes}</code>\n"
    rep += f"<b>Duration:</b> <code>{duration}</code>\n"
    rep += f"<b>Score:</b> <code>{score}</code>\n"
    rep += f"<b>Studio(s):</b> <code>{studios}</code>\n"
    rep += f"<b>Premiered:</b> <code>{premiered}</code>\n"
    rep += f"<b>Rating:</b> <code>{rating}</code>\n\n"
    rep += f"<a href='{image_url}'>\u200c</a>"
    rep += f"<i>{synopsis}</i>\n"
    await message.edit(rep, parse_mode='html')
    
    
