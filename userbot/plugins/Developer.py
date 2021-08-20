A = (
    "𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿 ====> @rintraccio ✅\n"
)

@catub.cat_cmd(
    pattern="Developer$",
    command=("Developer", plugin_category),
    info={
        "header": "Per vedere chi è il Developer",
        "usage": "{tr}Developer",
    },
)
async def bluedevilDeveloper(Developer):
    "fun art command"
    await edit_or_reply(Developer, A)
