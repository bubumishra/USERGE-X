#By @deleteduser420
""" Invert, filp/mirror, rotate """
import os
import time
from PIL import Image, ImageOps
from userge import userge, Message, Config
from userge.utils import progress, take_screen_shot, runcmd

@userge.on_cmd("(invert|mirror|flip)$", about={
    'header': "Invert, Mirror or Flip any media",
    'usage': "{tr}invert [reply to any media]\n"
             "{tr}mirror [reply to any media]\n"
             "{tr}flip [reply to any media]"}, name="transform")
async def transform(message: Message):
    replied = message.reply_to_message
    if not replied:
        await message.err("<code>Give Me Something to transform (¬_¬)</code>")
        await message.client.send_sticker(
            sticker="CAADAQADhgADwKwII4f61VT65CNGFgQ", chat_id=message.chat.id)
        return 
    if not (replied.photo or replied.sticker or replied.animation):
        await message.err("<code>Bruh You need help! I mean read HELP!</code>")
        return
    if not os.path.isdir(Config.DOWN_PATH):
        os.makedirs(Config.DOWN_PATH)
    transform_choice = message.matches[0].group(1).lower()
    choice_string = transform_choice.capitalize()
    await message.edit(f"<code>{choice_string}ing Media!...</code>")
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
            await message.err("<code>This sticker is BAKA, i won't Invert it ≧ω≦</code>")
            raise Exception(stdout + stderr)
        dls_loc = png_file

    elif replied.animation:
        await message.edit("<code>Look it's GF. Oh, no it's just a Gif</code>")
        jpg_file = os.path.join(Config.DOWN_PATH, "picture.jpg")
        await take_screen_shot(dls_loc, 0, jpg_file)
        os.remove(dls_loc)
        if not os.path.lexists(jpg_file):
            await message.err("<code>This Gif is  (｡ì _ í｡), won't invert it.</code>")
            return
        dls_loc = jpg_file
    webp_file = await transform_media(dls_loc, transform_choice)
    await message.client.send_sticker(chat_id=message.chat.id,
                                    sticker=webp_file,
                                    reply_to_message_id=replied.message_id)
    await message.delete()
    os.remove(webp_file)
    
async def transform_media(image_path, transform_choice):
    im = Image.open(image_path)
    os.remove(image_path)
    if not im.mode == 'RGB':
       im = im.convert('RGB')
    if transform_choice == "invert":
        out = ImageOps.invert(im)
    if transform_choice == "flip":    
        out = ImageOps.flip(im)
    else:
        out = im.transpose(Image.FLIP_LEFT_RIGHT)
    image_name = "invert.webp"
    webp_file = os.path.join(Config.DOWN_PATH, image_name)
    out.save(webp_file, "WebP")
    return webp_file

"""Rotate any media"""
@userge.on_cmd("rotate", about={
    'header': "Rotate any media",
    'usage': "{tr}rotate [angle to rotate] [reply to media]\n" 
             "angle = 0 to 360(default is 90)"})
    
async def rotate_(message: Message):
    replied = message.reply_to_message
    if not replied:
        await message.err("<code>Give Me Something to Rotate (¬_¬)</code>")
        await message.client.send_sticker(
            sticker="CAADAQADhgADwKwII4f61VT65CNGFgQ", chat_id=message.chat.id)
        return 
    if not (replied.photo or replied.sticker or replied.animation):
        await message.err("<code>Bruh You need help! I mean read HELP!</code>")
        return
    if message.input_str:
        input_ = int(message.input_str)
        if not message.input_str.isdigit():
            await message.err("```You input is invalid, check help...```", del_in=5)
            return
        if not 0 < input_ < 360:
            await message.err("```Invalid Angle...```", del_in=5)
            return
        args = input_
    else:
        args = 90
    if not os.path.isdir(Config.DOWN_PATH):
        os.makedirs(Config.DOWN_PATH)
   
    await message.edit(f"<code>Rotating Media by {args}°...</code>")
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
            await message.err("<code>This sticker is BAKA, i won't Rotate it ≧ω≦</code>")
            raise Exception(stdout + stderr)
        dls_loc = png_file

    elif replied.animation:
        await message.edit("<code>Look it's GF. Oh, no it's just a Gif</code>")
        jpg_file = os.path.join(Config.DOWN_PATH, "picture.jpg")
        await take_screen_shot(dls_loc, 0, jpg_file)
        os.remove(dls_loc)
        if not os.path.lexists(jpg_file):
            await message.err("<code>This Gif is wierd I can rotate it!</code>")
            return
        dls_loc = jpg_file
    webp_file = await rotate_media(dls_loc, args)
    await message.client.send_sticker(chat_id=message.chat.id,
                                    sticker=webp_file,
                                    reply_to_message_id=replied.message_id)
    await message.delete()
    os.remove(webp_file)
    
async def rotate_media(image_path, args):
    im = Image.open(image_path)
    os.remove(image_path)
    if not im.mode == 'RGB':
       im = im.convert('RGB')
    angle = args
    out = im.rotate(angle, expand=True)
    image_name = "rotated.webp"
    webp_file = os.path.join(Config.DOWN_PATH, image_name)
    out.save(webp_file, "WebP")
    return webp_file