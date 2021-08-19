import os

from telethon.errors.rpcerrorlist import UsernameOccupiedError
from telethon.tl import functions
from telethon.tl.functions.account import UpdateUsernameRequest
from telethon.tl.functions.channels import GetAdminedPublicChannelsRequest
from telethon.tl.functions.photos import DeletePhotosRequest, GetUserPhotosRequest
from telethon.tl.types import Channel, Chat, InputPhoto, User

from userbot import catub

from ..Config import Config
from ..core.logger import logging
from ..core.managers import edit_delete, edit_or_reply

LOGS = logging.getLogger(__name__)
plugin_category = "utils"


# ====================== CONSTANT ===============================
NAME_OK = "```Modalità offline attivata con successo```"
# ===============================================================


@catub.cat_cmd(
    pattern="offline ([\s\S]*)",
    command=("offline", plugin_category),
    info={
        "header": "To set offline mode.",
        "usage": ["{tr}offline"],
    },
)
async def _(event):
    "To set offline mode."
    names = event.pattern_match.group(1)
    first_name = __name__ OFF
    last_name = ""
    if ";" in names:
        first_name, last_name = names.split(";", 1)
    try:
        await event.client(
            functions.account.UpdateProfileRequest(
                first_name=first_name, last_name=last_name
            )
        )
        await edit_delete(event, "`Il mio nome è stato cambiato con successo!`")
    except Exception as e:
        await edit_or_reply(event, f"**Error:**\n`{e}`")
