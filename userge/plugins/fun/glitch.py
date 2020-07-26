#by @deleteduser420

import os
import time
from PIL import Image, ImageFont, ImageDraw
from glitch_this import ImageGlitcher
from userge import userge, Message, Config
from userge.utils import progress
import numpy as np
glitcher = ImageGlitcher()
'''Reply to an Media and see the Magic'''
@userge.on_cmd("glitch", about={
    'header': "Glitch any media",
    'usage': "{tr}Glitch [glitch level i.e 1-8] [reply to media]",
    'example': "{tr}glitch 2"})
async def glitch_this(message: Message):
    replied = message.reply_to_message
    if message.input_str:
        input_ = int(message.input_str)
        if not message.input_str.isdigit():
            await message.err("```You input is invalid, check help...```", del_in=5)
            return
        if not 1 <= input_ <= 8:
            await message.err("```Invalid Angle...```", del_in=5)
            return
        glevel = input_
    else:
        glevel = 1
    if not os.path.isdir(Config.DOWN_PATH):
        os.makedirs(Config.DOWN_PATH)
    await message.edit(f"<code>Converting Media!...</code>")
    c_time = time.time()

    dls = await message.client.download_media(
        message=message.reply_to_message,
        file_name=Config.DOWN_PATH,
        progress=progress,
        progress_args=(
            "Trying to Posses given content", userge, message, c_time
        )
    )
    dls_loc = os.path.join(Config.DOWN_PATH, os.path.basename(dls))
    
   
    if replied.sticker and replied.sticker.file_name.endswith(".tgs"):
        await message.edit("<code>OMG, an Animated sticker ⊙_⊙, lemme do my megik...</code>")
        png_file = os.path.join(Config.DOWN_PATH, "picture.png")
        cmd = f"lottie_convert.py --frame 0 -if lottie -of png {dls_loc} {png_file}"
        stdout, stderr = (await runcmd(cmd))[:2]
        os.remove(dls_loc)
        if not os.path.lexists(png_file):
            await message.err("<code>This sticker is BAKA, i won't Glitch it ≧ω≦</code>")
            raise Exception(stdout + stderr)
        dls_loc = png_file
        
        
    elif replied.animation:
        await message.edit("<code>Look it's GF. Oh, no it's just a Gif</code>")
        jpg_file = os.path.join(Config.DOWN_PATH, "picture.jpg")
        await take_screen_shot(dls_loc, 0, jpg_file)
        os.remove(dls_loc)
        if not os.path.lexists(jpg_file):
            await message.err("<code>This Gif is  (｡ì _ í｡), won't Glitch it.</code>")
            return
        dls_loc = jpg_file
        

    webp_file = glitch_fun(dls_loc, glevel)
    await message.client.send_animation(chat_id=message.chat.id,
                                    animation=webp_file,
                                    reply_to_message_id=replied.message_id)
    await message.delete()
    os.remove(webp_file)
    os.remove(dls_loc)

def glitch_fun(file_name, glevel):
    img = Image.open(file_name)
    glitch_level = glevel
    glitch_img = glitcher.glitch_image(img, glitch_level, color_offset=True, gif=True)


    DURATION = 200      # Set this to however many centiseconds each frame should be visible for
    LOOP = 0            # Set this to how many times the gif should loop
                        # LOOP = 0 means infinite loop
    image_name = "glitched_test.gif"                    
    gif_file = os.path.join(Config.DOWN_PATH, image_name)
    glitch_img[0].save(gif_file,
                    format='GIF',
                    append_images=glitch_img[1:],
                    save_all=True,
                    duration=DURATION,
                    loop=LOOP)
    return gif_file

