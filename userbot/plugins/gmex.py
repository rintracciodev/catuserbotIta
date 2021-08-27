from telethon import functions, types
from userbot.events import register
import os, json, asyncio

if os.path.exists("gruppigmex.json"):
    with open("gruppigmex.json", "r+") as f:
        Groups = json.load(f)
else:
    Groups = {}
    with open("gruppigmex.json", "w+") as f:
      json.dump(Groups, f)

async def updateGroups():
    global Groups
    with open("gruppigmex.json", "w+") as f:
        json.dump(Groups, f)
    return True

@register(outgoing=True, pattern="^[.]gmex")
async def GmexFunction(e):
    global Groups
    st = e.text.split(" ", 1)
    if len(st) == 2:
        if len(Groups) > 0:
            await e.edit("**⚠️ Avviso** » __Sto gmexando, Attendere...__")
            await asyncio.wait([e.client.send_message(int(chat), st[1]) for chat in Groups])
            await e.edit("**✅ » Gmex completato con successo!**")
        else:
            await e.edit("**⚠️ Errore** » __Non ci sono gruppi in cui gmexare!__")
    else:
         await e.edit("**⚠️ Errore** » __Specifica il messaggio che devo gmexare!__")

@register(outgoing=True, pattern="^[.]addgroup")
async def addChat(e):
    global Groups
    st = e.text.replace("-100", "").split(" ", 1)
    if len(st) == 2:
        if st[1].isnumeric():
            mex = int(st[1])
        else:
            mex = st[1]
        try:
            group = await e.client.get_entity(mex)
        except:
            await e.edit(f"**⚠️ Errore** » __Chat non trovata, controlla di aver inserito l'username/ID corretto!__")
            return
        if type(group).__name__ == "User":
            await e.edit("**⚠️ Errore** » __Puoi aggiungere solo gruppi o canali!__")
            return
        if not str(group.id) in Groups:
            Groups[str(group.id)] = group.title
            await updateGroups()
            await e.edit(f"**✅ » Chat** {group.title} **aggiunta con successo!**")
        else:
            await e.edit(f"**⚠️ Errore** » __Chat__ {group.title} __già presente nel database__")
    else:
        await e.edit("**⚠️ Errore** » __Specifica la chat da aggiungere!__")

@register(outgoing=True, pattern="^[.]delgroup")
async def remChat(e):
    global Groups
    st = e.text.replace("-100", "").split(" ", 1)
    if len(st) == 2:
        if st[1].isnumeric():
            mex = int(st[1])
        else:
            mex = st[1]
        try:
            group = await e.client.get_entity(mex)
        except:
            await e.edit("**⚠️ Errore** »__Chat non trovata__ ")
            return
        if str(group.id) in Groups:
            del Groups[str(group.id)]
            await updateGroups()
            await e.edit(f"**🚫 » Chat** {group.title} **rimossa con successo!**")
        else:
            await e.edit(f"**⚠️ Errore** » __Chat__ {group.title} __non presente nel database__**")
    else:
        await e.edit("**⚠️ Errore** » __Specifica la Chat da rimuovere!__")

@register(outgoing=True, pattern="^[.]group$")
async def chatsList(e):
    global Groups
    if len(Groups) > 0:
        msg = "**💬 LISTA CHAT 💬**\n"
        for id in Groups:
            msg += "\n" + Groups[id] + f" [`-100{id}`]"
        await e.edit(msg + "\n\n__📂 Chat Totali  »__ `" + str(len(Groups)) + "`")
    else:
        await e.edit("**⚠️ Nessuna Chat Aggiunta ⚠️**")