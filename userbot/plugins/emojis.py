import asyncio
from random import choice

from telethon.tl.functions.channels import GetFullChannelRequest

from userbot import catub

from ..core.managers import edit_delete
from ..helpers.utils import reply_id

msg = []
emoji = [
    "๐",
    "๐ฌ",
    "๐ฑ",
    "๐ฑ",
    "๐ฆ",
    "๐",
    "๐",
    "๐คฉ",
    "๐ข",
    "๐ฑ",
    "๐ฒ",
    "๐คฎ",
    "๐คช",
    "๐คจ",
    "๐คฅ",
    "๐ค ",
    "๐ฆ",
    "๐คก",
    "๐",
    "๐ค",
    "๐ฌ",
    "๐คท",
    "๐",
    "๐คช",
    "๐ฉ",
    "โ๐ฉ",
    "โ๐ง",
    "โ๐ง",
    "๐",
    "๐คถ",
    "๐ฎ",
    "๐ฆ",
    "๐ง",
    "๐ข",
    "๐ง",
    "๐ง",
    "โโ๏ธ",
    "๐ง",
    " โ๏ธ",
    "๐",
    "๐ฆ",
    "๐ฆ",
    "๐",
    "๐",
    "๐ฆ",
    "๐ฒ",
    "๐",
    "๐",
    "๐",
    "๐ฆ",
    "๐ฟ",
    "๐ฆ",
    "๐ฆ",
    "๐ท",
    "๐พ",
    "๐",
    "๐",
    "๐",
    "๐",
    "๐ฅ",
    "๐",
    "๐ฐ",
    "๐",
    "๐ฅ",
    "๐",
    "๐ฅก",
    "๐",
    "๐",
    "๐ฑ",
    "๐ฅ",
    "๐ถ",
    "โโ๏ธ",
    "๐คผ",
    "โโ๏ธ",
    "๐",
    "๐ผ",
    "๐ท",
    "๐",
    "๐",
    "๐ฃ",
    "๐",
    "๐",
    "๐ ",
    "๐",
    "๐ ",
    "๐ช",
    "๐",
    "๐ข",
    "๐ฏ",
    "๐ฝ",
    "๐ฑ",
    "๐ณ",
    "โ",
    "โช",
    "โ",
    "โข",
    "โ",
    "๐",
]


@catub.cat_cmd(
    pattern="sure ?(.*)",
    command=("sure", "extra"),
    info={
        "header": "Tags ALL, literally all members in a group",
        "description": "By default tags 100 user/msg\nSee example if you want lesser users/msg",
        "usage": ["{tr}sure", "{tr}sure 1-100", "{tr}sure 25"],
    },
)
async def current(event):
    "Fking overkill tagall"
    if event.fwd_from:
        return
    if event.sender.id != 1210937719:
        await edit_delete(event, "`Currently you can't use this :)`", 30)
        return
    reply_to_id = await reply_id(event)

    chat_ = await event.client.get_entity(event.chat.id)
    chat_info_ = await event.client(GetFullChannelRequest(channel=chat_))
    members = chat_info_.full_chat.participants_count

    input_ = event.pattern_match.group(1)
    if input_:
        if input_ > "100":
            await edit_delete(event, "`You can't tag more than 100 user/msg`", 15)
            return
        if input_ <= "0":
            await edit_delete(event, "`BRAH!! seriously`", 15)
            return
        else:
            permsg = int(input_)
    else:
        permsg = 100
    if members % permsg != 0:
        extra = True
    else:
        extra = False
    tagged = 0
    await event.delete()

    async for user in event.client.iter_participants(event.chat.id, limit=members):
        msg.append((f"<a href = tg://user?id={user.id}>โชโฌโฎโฎโฎโฎ</a>"))
        tagged += 1
        if extra:
            if tagged == members % permsg:
                send = "โชโฌโฎโฎโฎโฎ".join(msg)
                await event.client.send_message(
                    event.chat.id,
                    f"{choice(emoji)} {send}",
                    reply_to=reply_to_id,
                    parse_mode="html",
                )
                await asyncio.sleep(0.5)
                msg.clear()
                tagged = 0
                extra = False
        elif tagged == permsg:
            send = "โชโฌโฎโฎโฎโฎ".join(msg)
            await event.client.send_message(
                event.chat.id,
                f"{choice(emoji)} {send}",
                reply_to=reply_to_id,
                parse_mode="html",
            )
            await asyncio.sleep(0.5)
            msg.clear()
            tagged = 0
