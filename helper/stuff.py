#    This file is part of the CompressorBot distribution.
#    Copyright (c) 2021 Danish_00
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
#    License can be found in < https://github.com/1Danish-00/CompressorBot/blob/main/License> .

from .worker import *
#from telethon.tl.functions.users import GetFullUserRequest
from telethon import Button
from datetime import datetime as dt

# Ping command
async def up(event):
    if not event.is_private:
        return
    stt = dt.now()
    ed = dt.now()
    v = ts(int((ed - uptime).seconds) * 1000)
    ms = (ed - stt).microseconds / 1000
    p = f"🌋Pɪɴɢ = {ms}ms"
    await event.reply(v + "\n" + p)

# Start command
async def start(event):
    user = await event.get_sender()
    await event.reply(
        f"Hi `{user.first_name}`\nThis is A CompressorBot Which Can Encode Videos.\nReduce Size of Videos With Negligible Quality Change\nU can Generate Samples/screenshots too.",
        buttons=[
            [Button.inline("HELP", data="ihelp")],
            [
                Button.url("SOURCE CODE", url="https://github.com/1Danish-00/CompressorBot"),
                Button.url("DEVELOPER", url="https://t.me/danish_00"),
            ],
        ],
    )

# Help command
async def help(event):
    await event.reply(
        "**🐠 A Quality CompressorBot**\n\n"
        "+ This Bot Compresses Videos With Negligible Quality Change.\n"
        "+ Generate Sample Compressed Video\n"
        "+ Easy to Use\n"
        "- Due to Quality Settings, Bot Takes Time To Compress.\n"
        "So Be Patient And Send Videos One By One After Completing.\n"
        "Don't Spam the Bot.\n\n"
        "Just Forward a Video To Get Options"
    )

# Inline help
async def ihelp(event):
    await event.edit(
        "**🐠 A Quality CompressorBot**\n\n"
        "+ This Bot Compresses Videos With Negligible Quality Change.\n"
        "+ Generate Sample Compressed Video\n"
        "+ Screenshots Too\n"
        "+ Easy to Use\n"
        "- Due to Quality Settings, Bot Takes Time To Compress.\n"
        "So Be Patient And Send Videos One By One After Completing.\n"
        "Don't Spam the Bot.\n\n"
        "Just Forward a Video To Get Options",
        buttons=[Button.inline("BACK", data="beck")],
    )

# Back to main menu
async def beck(event):
    user = await event.get_sender()
    await event.edit(
        f"Hi `{user.first_name}`\nThis is A CompressorBot Which Can Encode Videos.\nReduce Size of Videos With Negligible Quality Change\nU can Generate Samples/screenshots too.",
        buttons=[
            [Button.inline("HELP", data="ihelp")],
            [
                Button.url("SOURCE CODE", url="https://github.com/1Danish-00/"),
                Button.url("DEVELOPER", url="https://t.me/danish_00"),
            ],
        ],
    )

# Compression mode selection
async def sencc(e):
    key = e.pattern_match.group(1).decode("UTF-8")
    await e.edit(
        "Choose Mode",
        buttons=[
            [
                Button.inline("Default Compress", data=f"encc{key}"),
                Button.inline("Custom Compress", data=f"ccom{key}"),
            ],
            [Button.inline("Back", data=f"back{key}")],
        ],
    )

# Back to video options
async def back(e):
    key = e.pattern_match.group(1).decode("UTF-8")
    await e.edit(
        "🐠  **What To Do** 🐠",
        buttons=[
            [
                Button.inline("GENERATE SAMPLE", data=f"gsmpl{key}"),
                Button.inline("SCREENSHOTS", data=f"sshot{key}"),
            ],
            [Button.inline("COMPRESS", data=f"sencc{key}")],
        ],
    )


async def ccom(e):
    await e.edit("Send Ur Custom Name For That File")
    wah = e.pattern_match.group(1).decode("UTF-8")
    wh = decode(wah)
    out, dl, thum, dtime = wh.split(";")
    chat = e.sender_id
    async with e.client.conversation(chat) as cv:
        reply = cv.wait_event(events.NewMessage(from_users=chat))
        repl = await reply
        if "." in repl.text:
            q = repl.text.split(".")[-1]
            g = repl.text.replace(q, "mkv")
        else:
            g = repl.text + ".mkv"
        outt = f"encode/{chat}/{g}"
        x = await repl.reply(
            f"Custom File Name : {g}\n\nSend Thumbnail Picture For it."
        )
        replyy = cv.wait_event(events.NewMessage(from_users=chat))
        rep = await replyy
        if rep.media:
            tb = await e.client.download_media(rep.media, f"thumb/{chat}.jpg")
        elif rep.text and not (rep.text).startswith("/"):
            url = rep.text
            os.system(f"wget {url}")
            tb = url.replace("https://telegra.ph/file/", "")
        else:
            tb = thum
        omk = await rep.reply(f"Thumbnail {tb} Setted Successfully")
        hehe = f"{outt};{dl};{tb};{dtime}"
        key = code(hehe)
        await customenc(omk, key)
