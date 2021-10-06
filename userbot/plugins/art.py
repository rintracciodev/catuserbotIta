from . import ALIVE_NAME, catub, edit_or_reply

plugin_category = "fun"


@catub.cat_cmd(
    pattern="ded ([\s\S]*)",
    command=("ded", plugin_category),
    info={
        "header": "Just a art command try out yourself to see",
        "usage": "{tr}ded <text>",
    },
)
async def _(event):
    "fun art command"
    name = event.pattern_match.group(1)
    await edit_or_reply(
        event,
        f"{ALIVE_NAME} --- {name}          \n　　　　　|"
        "\n　　　　　| \n"
        "　　　　　| \n"
        "　　　　　| \n"
        "　　　　　| \n"
        "　　　　　| \n"
        "　　　　　| \n"
        "　　　　　| \n"
        "　／￣￣＼| \n"
        "＜ ´･ 　　 |＼ \n"
        "　|　３　 | 丶＼ \n"
        "＜ 、･　　|　　＼ \n"
        "　＼＿＿／∪ _ ∪) \n"
        "　　　　　 Ｕ Ｕ\n",
    )


@catub.cat_cmd(
    pattern="killer ([\s\S]*)",
    command=("killer", plugin_category),
    info={
        "header": "Just a art command try out yourself to see",
        "usage": "{tr}killer <text>",
    },
)
async def _(event):
    "fun art command"
    name = event.pattern_match.group(1)
    await edit_or_reply(
        event,
        f"__**Commando **__{ALIVE_NAME}          \n\n"
        "_/﹋\_\n"
        "(҂`_´)\n"
        f"<,︻╦╤─ ҉ - - - {name}\n"
        "_/﹋\_\n",
    )


A = (
    "▄███████▄\n"
    "█▄█████▄█\n"
    "█▼▼▼▼▼█\n"
    "██________█▌\n"
    "█▲▲▲▲▲█\n"
    "█████████\n"
    "_████\n"
)

B = (
    "┈┈┏━╮╭━┓┈╭━━━━╮\n"
    "┈┈┃┏┗┛┓┃╭┫ⓞⓘⓝⓚ┃\n"
    "┈┈╰┓▋▋┏╯╯╰━━━━╯\n"
    "┈╭━┻╮╲┗━━━━╮╭╮┈\n"
    "┈┃▎▎┃╲╲╲╲╲╲┣━╯┈\n"
    "┈╰━┳┻▅╯╲╲╲╲┃┈┈┈\n"
    "┈┈┈╰━┳┓┏┳┓┏╯┈┈┈\n"
    "┈┈┈┈┈┗┻┛┗┻┛┈┈┈┈\n"
)

D = (
    "░▐█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█▄\n"
    "░███████████████████████ \n"
    "░▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓◤ \n"
    "░▀░▐▓▓▓▓▓▓▌▀█░░░█▀░\n"
    "░░░▓▓▓▓▓▓█▄▄▄▄▄█▀░░\n"
    "░░█▓▓▓▓▓▌░░░░░░░░░░\n"
    "░▐█▓▓▓▓▓░░░░░░░░░░░\n"
    "░▐██████▌░░░░░░░░░░\n"
)

E = (
    "╥━━━━━━━━╭━━╮━━┳\n"
    "╢╭╮╭━━━━━┫┃▋▋━▅┣\n"
    "╢┃╰┫┈┈┈┈┈┃┃┈┈╰┫┣\n"
    "╢╰━┫┈┈┈┈┈╰╯╰┳━╯┣\n"
    "╢┊┊┃┏┳┳━━┓┏┳┫┊┊┣\n"
    "╨━━┗┛┗┛━━┗┛┗┛━━┻\n"
)
F = "╔┓┏╦━╦┓╔┓╔━━╗\n" "║┗┛║┗╣┃║┃║X X║\n" "║┏┓║┏╣┗╣┗╣╰╯║\n" "╚┛┗╩━╩━╩━╩━━╝\n"
G = (
    "▬▬▬.◙.▬▬▬ \n"
    "═▂▄▄▓▄▄▂ \n"
    "◢◤ █▀▀████▄▄▄▄◢◤ \n"
    "█▄ █ █▄ ███▀▀▀▀▀▀▀╬ \n"
    "◥█████◤ \n"
    "══╩══╩══ \n"
    "╬═╬ \n"
    "╬═╬ \n"
    "╬═╬ \n"
    "╬═╬ \n"
    "╬═╬ \n"
    "╬═╬ \n"
    "╬═╬ Perchè non implodi ? :D \n"
    "╬═╬☻/ \n"
    "╬═╬/▌ \n"
    "╬═╬/ \\n"
)

H = (
    "┳┻┳┻╭━━━━╮╱▔▔▔╲\n"
    "┻┳┻┳┃╯╯╭━┫▏╰╰╰▕\n"
    "┳┻┳┻┃╯╯┃▔╰┓▔▂▔▕╮\n"
    "┻┳┻┳╰╮╯┃┈╰┫╰━╯┏╯\n"
    "┳┻┳┻┏╯╯┃╭━╯┳━┳╯\n"
    "┻┳┻┳╰━┳╯▔╲╱▔╭╮▔╲\n"
    "┳┻┳┻┳┻┃┈╲┈╲╱╭╯╮▕\n"
    "┻┳┻┳┻┳┃┈▕╲▂╱┈╭╯╱\n"
    "┳┻┳┻┳┻┃'''┈┃┈┃┈'''╰╯\n"
    "┻┳┻┳┻┏╯▔'''╰┓┣━┳┫\n"
    "┳┻┳┻┳╰┳┳┳'''╯┃┈┃┃\n"
    "┻┳┻┳┻┳┃┃┃┈'''┃┈┃┃\n"
    "┳┻┳┻┳┻┃┃┃'''┊┃┈┃┃\n"
    "┻┳┻┳┻┳┃┃┃┈'''┃┈┃┃.\n"
    "┳┻┳┻┳┻┣╋┫'''┊┣━╋┫\n"
    "┻┳┻┳┻╭╯╰╰-╭╯━╯.''╰╮\n"
    "Love You Forever,,,,\n"
)

I = (
    "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⡿⠋⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⠀⠀⣠⣾⣿⡿⠋⠀⠀⠉⠻⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⠀⠀⣿⣿⣿⠃⠀⠀⣀⡀⠀⢹⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⡄⠀⠙⠻⠋⠀⠀⣸⣿⣿⠀⠀⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⣰⣿⣿⠟⠀⢠⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⡿⠛⠛⠒⠶⠾⢿⣿⣿⣷⣄⣾⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⠀⢰⣿⣿⣷⣶⣦⣼⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⡀⠀⠙⠻⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⢿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⠀⠀⠀⠉⠉⠛⠛⠛⠶⢶⣤⣼⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣦⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⠁⠀⣾⣿⣷⡄⠀⢼⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⠀⠀⢿⣿⣿⡿⠀⠈⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⣇⠀⠀⠉⠋⠁⠀⢠⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⠿⢷⣤⣀⣀⣀⣠⣾⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⠀⠀⠀⠈⠉⠉⠛⢻⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⣶⣦⣤⣤⣀⠀⠀⢸⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠹⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⡿⠛⠉⠉⠙⠻⣀⣀⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⠁⠀⣀⡀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⠀⢸⣿⡇⠀⣷⡀⠘⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⡄⠈⢻⡇⠀⡿⠃⠀⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⣷⣄⢸⡇⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⠀⠉⠉⠑⠒⠲⠿⢿⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⣤⣄⣀⡀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⢺⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⠀⠀⠉⠉⠙⠋⠀⠀⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⣤⣤⣀⣀⡀⠀⠀⣰⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣷⠀⢹⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⠀⠀⠀⠉⠉⠉⠀⠀⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⣶⣤⣤⣀⣀⣀⣀⣰⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⡟⠉⠀⠀⠈⠙⢿⣿⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⠀⢀⣤⡄⠀⡀⠀⢹⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⠀⢸⣿⡇⠀⣿⡄⠈⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⡆⠀⢹⡇⠀⠟⠁⢀⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⣿⣦⣸⡇⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
)

J = (
    "⣿⣿⣿⣿⣿⣍⠀⠉⠻⠟⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⠓⠀⠀⢒⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⣿\n"
    "⣿⡿⠋⠋⠀⠀⠀⠀⠀⠀⠈⠙⠻⢿⢿⣿⣿⡿⣿⣿⡟⠋⠀⢀⣩\n"
    "⣿⣿⡄⠀⠀⠀⠀⠀⠁⡀⠀⠀⠀⠀⠈⠉⠛⢷⣭⠉⠁⠀⠀⣿⣿\n"
    "⣇⣀. INDIA🇮🇳INDIA🇮🇳⠆⠠..⠘⢷⣿⣿⣛⠐⣶⣿⣿\n"
    "⣿⣄⠀⣰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⢀⣠⣿⣿⣿⣾⣿⣿⣿\n"
    "⣿⣿⣿⣿⠀⠀⠀⠀⡠⠀⠀⠀⠀⠀⢀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠄⠀⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⣠⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⠀⠀⠂⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣇⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⡆⠀⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⣿⣦⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
)

K = (
    "───▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄───\n"
    "───█▒▒░░░░░░░░░▒▒█───\n"
    "────█░░█░░░░░█░░█────\n"
    "─▄▄──█░░░▀█▀░░░█──▄▄─\n"
    "█░░█─▀▄░░░░░░░▄▀─█░░█\n"
    "█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█\n"
    "█░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█\n"
    "█░░║║║╠─║─║─║║║║║╠─░░█\n"
    "█░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█\n"
    "█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n"
)

L = (
    "░░░░▓\n"
    "░░░▓▓\n"
    "░░█▓▓█\n"
    "░██▓▓██\n"
    "░░██▓▓██\n"
    "░░░██▓▓██\n"
    "░░░░██▓▓██\n"
    "░░░░░██▓▓██\n"
    "░░░░██▓▓██\n"
    "░░░██▓▓██\n"
    "░░██▓▓██\n"
    "░██▓▓██\n"
    "░░██▓▓██\n"
    "░░░██▓▓██\n"
    "░░░░██▓▓██\n"
    "░░░░░██▓▓██\n"
    "░░░░██▓▓██\n"
    "░░░██▓▓██\n"
    "░░██▓▓██\n"
    "░██▓▓██\n"
    "░░██▓▓██\n"
    "░░░██▓▓██\n"
    "░░░░██▓▓██\n"
    "░░░░░██▓▓██\n"
    "░░░░██▓▓██\n"
    "░░░██▓▓██\n"
    "░░██▓▓██\n"
    "░██▓▓██\n"
    "░░██▓▓██\n"
    "░░░██▓▓██\n"
    "░░░░██▓▓██\n"
    "░░░░░██▓▓██\n"
    "░░░░██▓▓██\n"
    "░░░██▓▓██\n"
    "░░██▓▓██\n"
    "░██▓▓██\n"
    "░░██▓▓██\n"
    "░░░██▓▓██\n"
    "░░░░██▓▓██\n"
    "░░░░░██▓▓██\n"
    "░░░░██▓▓██\n"
    "░░░██▓▓██\n"
    "░░██▓▓██\n"
    "░██▓▓██\n"
    "░░██▓▓██\n"
    "░░░██▓▓██\n"
    "░░░░██▓▓██\n"
    "░░░░░██▓▓██\n"
    "░░░░██▓▓██\n"
    "░░░██▓▓██\n"
    "░░██▓▓██\n"
    "░██▓▓██\n"
    "░░██▓▓██\n"
    "░░░██▓▓██\n"
    "░░░░██▓▓██\n"
    "░░░░░██▓▓██\n"
    "░░░░██▓▓██\n"
    "░░░██▓▓██\n"
    "░░██▓▓██\n"
    "░██▓▓██\n"
    "░░██▓▓██\n"
    "░░░██▓▓██\n"
    "░░░░██▓▓██\n"
    "░░░░░██▓▓██\n"
    "░░░░██▓▓██\n"
    "░░░██▓▓██\n"
    "░░██▓▓██\n"
    "░░██▓▓██\n"
    "░░██▓▓██\n"
    "░░██▓▓██\n"
    "░░██▓▓██\n"
    "░░██▓▓██\n"
    "░░░██▓▓███\n"
    "░░░░██▓▓████\n"
    "░░░░░██▓▓█████\n"
    "░░░░░░██▓▓██████\n"
    "░░░░░░███▓▓███████\n"
    "░░░░░████▓▓████████\n"
    "░░░░█████▓▓█████████\n"
    "░░░█████░░░█████●███\n"
    "░░████░░░░░░░███████\n"
    "░░███░░░░░░░░░██████\n"
    "░░██░░░░░░░░░░░████\n"
    "░░░░░░░░░░░░░░░░███\n"
    "░░░░░░░░░░░░░░░░░░░\n"
)


O = (
    "────██──────▀▀▀██\n"
    "──▄▀█▄▄▄─────▄▀█▄▄▄\n"
    "▄▀──█▄▄──────█─█▄▄\n"
    "─▄▄▄▀──▀▄───▄▄▄▀──▀▄\n"
    "─▀───────▀▀─▀───────▀▀\n🚶🏻‍♂️🚶🏻‍♂️ɮʏɛ ʄʀɨɛռɖֆ.."
)

P = (
    "╭━━━┳╮╱╱╭╮╱╭━━━┳━━━╮\n"
    "┃╭━╮┃┃╱╭╯╰╮┃╭━╮┃╭━╮┃\n"
    "┃╰━━┫╰━╋╮╭╯┃┃╱┃┃╰━━╮\n"
    "╰━━╮┃╭╮┣┫┃╱┃┃╱┃┣━━╮┃\n"
    "┃╰━╯┃┃┃┃┃╰╮┃╰━╯┃╰━╯┃\n"
    "╰━━━┻╯╰┻┻━╯╰━━━┻━━━╯\n"
)


R = (
    "███████▄▄███████████▄\n"
    "▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n"
    "▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n"
    "▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n"
    "▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n"
    "▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n"
    "▓▓▓▓▓▓███░░░░░░░░░░░░█\n"
    "██████▀░░█░░░░██████▀\n"
    "░░░░░░░░░█░░░░█\n"
    "░░░░░░░░░░█░░░█\n"
    "░░░░░░░░░░░█░░█\n"
    "░░░░░░░░░░░█░░█\n"
    "░░░░░░░░░░░░▀▀\n"
)


S = (
    "╱┏┓╱╱╱╭━━━╮┏┓╱╱╱╱\n"
    "╱┃┃╱╱╱┃╭━╮┃┃┃╱╱╱╱\n"
    "╱┃┗━━┓┃╰━╯┃┃┗━━┓╱\n"
    "╱┗━━━┛╰━━━╯┗━━━┛╱\n"
)    


T = (
    
    "░█▀▀█ ▀█▀░█▀▀█\n"
    "░█▄▄▀ ░█   ░█▄▄█\n"
    "░█ ░█   ▄█▄░█ ░ \n"
)
    
    
U = (
    "──────────────────────\n"
    "─────────────███──────\n"
    "─────────────███──────\n"
    "──────▄█████▄█▀▀──────\n"
    "───────▀█████─────────\n"
    "────────▄████▄────────\n"
)


V = (
    "🧑‍💻 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿 ====> @rintraccio ✅\n"
)


W = (
    "🔱Middleman = admin = escrow🔱\n"
    "È un terzo che fa da tramite in uno scambio (vendita o acquisto) per garantire sicurezza ad entrambi. Il mm deve avere feed.\n"
    "             \n"
    "☔️Esempio:☔️\n"
    "             \n"
    "Io do il mio metodo al mm\n"
    "Tu dai i soldi al mm. Il mm controlla se il metodo va.\n"
    "Se non ci sono problemi l'mm ti invia il metodo e io ricevo i soldi.\n"
)


X = (
    "🚷Motivazioni netban:\n"
    "            \n"
    "•Tentata truffa\n"
    "•Ammisione truffa\n"
    "•Truffa\n"
    "•Dox\n"
    "•Fake netban\n" 
    "•Fake admin\n"
    "•Fake rep\n"
    "•Fake di @\n"
    "•Fake MM\n"
    "•Voip di @\n"
    "•Main di @\n"
    "•Violazione T.o.S\n"
    "•Refuse di MM\n"
    "•Grief\n"
    "•Storm\n"
    "•Divulgazione di dati personali\n"
)


Y = (
    "┈┈┏━╮╭━┓┈╭━━━━━━━━━━━━━━━━━━━━━━━━━━━╮\n"
    "┈┈┃┏┗┛┓┃╭┫Mi chiamo Vederico Vaiana !┃\n"
    "┈┈╰┓▋▋┏╯╯╰━━━━━━━━━━━━━━━━━━━━━━━━━╯\n"
    "┈╭━┻╮╲┗━━━━╮╭╮┈\n"
    "┈┃▎▎┃╲╲╲╲╲╲┣━╯┈\n"
    "┈╰━┳┻▅╯╲╲╲╲┃┈┈┈\n"
    "┈┈┈╰━┳┓┏┳┓┏╯┈┈┈\n"
    "┈┈┈┈┈┗┻┛┗┻┛┈┈┈┈\n"
)    

    
Z = (
    " ██▄█╔═╗█▀█╔═╗█──╔╗─██▄█╔═╗█──▄█▀█▄▄███▄\n"
    " █─▀█║█║██▀║█║█──║║─█─▀█║═╣█─▐█░████████\n"
    " █──█║╦║█──║▀║███║║─█──█║═╣███▀████████▀\n"
    " ────╚╩╝───╚═╝───╚╝─────╚═╝──────▀██▀__\n"
    "__________$$$$$$$$$$$$$$$$$$$$$\n"
    "_______$$$$$$$$$$$$$$$$$$$$$$$$$$$\n"
    "_____$$$$$$$$$________________$$$$$$$\n"
    "____$$$$$$$_______________________$$$$$\n"
    "___$$$$$$_¶¶¶¶¶¶¶¶_____________¶¶¶¶_$$$$\n"
    "__$$$$$___¶¶¶¶_¶¶¶¶____________¶¶¶¶__$$$$\n"
    "_$$$$$____¶¶¶¶__¶¶¶¶___________¶¶¶¶___$$$$\n"
    "$$$$$_____¶¶¶¶___¶¶¶¶__________¶¶¶¶____$$$$\n"
    "$$$$______¶¶¶¶____¶¶¶¶_________¶¶¶¶____$$$$\n"
    "$$$$______¶¶¶¶_____¶¶¶¶________¶¶¶¶____$$$$\n"
    "$$$$______¶¶¶¶______¶¶¶¶_______¶¶¶¶____$$$$\n"
    "$$$$______¶¶¶¶_______¶¶¶¶______¶¶¶¶____$$$$\n"
    "$$$$______¶¶¶¶________¶¶¶¶_____¶¶¶¶____$$$$\n"
    "$$$$______¶¶¶¶_________¶¶¶¶____¶¶¶¶____$$$$\n"
    "$$$$$_____¶¶¶¶__________¶¶¶¶___¶¶¶¶___$$$$\n"
    "_$$$$_____¶¶¶¶___________¶¶¶¶__¶¶¶¶__$$$$\n"
    "__$$$$$___¶¶¶¶____________¶¶¶¶_¶¶¶¶_$$$$$\n"
    "__$$$$$$__¶¶¶¶_____________¶¶¶¶¶¶¶¶$$$$$\n"
    "____$$$$$$¶¶¶¶______________¶¶¶¶¶¶¶$$$$\n"
    "_____$$$$$$$____________________$$$$$$$\n"
    "_______$$$$$$$$$$__________$$$$$$$$$\n"
    "_________$$$$$$$$$$$$$$$$$$$$$$$$$\n"
    "_____________$$$$$$$$$$$$$$$$$\n"
    
    
@catub.cat_cmd(   
    pattern="monster$",
    command=("monster", plugin_category),
    info={
        "header": "Just a art command try out yourself to see",
        "usage": "{tr}monster",
    },
)
async def bluedevilmonster(monster):
    "fun art command"
    await edit_or_reply(monster, A)


@catub.cat_cmd(
    pattern="pig$",
    command=("pig", plugin_category),
    info={
        "header": "Just a art command try out yourself to see",
        "usage": "{tr}pig",
    },
)
async def bluedevilpig(pig):
    "fun art command"
    await edit_or_reply(pig, B)


@catub.cat_cmd(
    pattern="gun$",
    command=("gun", plugin_category),
    info={
        "header": "Just a art command try out yourself to see",
        "usage": "{tr}gun",
    },
)
async def bluedevilgun(gun):
    "fun art command"
    await edit_or_reply(gun, D)


@catub.cat_cmd(
    pattern="dog$",
    command=("dog", plugin_category),
    info={
        "header": "Just a art command try out yourself to see",
        "usage": "{tr}dog",
    },
)
async def bluedevildog(dog):
    "fun art command"
    await edit_or_reply(dog, E)


@catub.cat_cmd(
    pattern="hello$",
    command=("hello", plugin_category),
    info={
        "header": "Just a art command try out yourself to see",
        "usage": "{tr}hello",
    },
)
async def bluedevilhello(hello):
    "fun art command"
    await edit_or_reply(hello, F)


@catub.cat_cmd(
    pattern="heli$",
    command=("heli", plugin_category),
    info={
        "header": "Just a art command try out yourself to see",
        "usage": "{tr}heli",
    },
)
async def bluedevilheli(heli):
    "fun art command"
    await edit_or_reply(heli, G)


@catub.cat_cmd(
    pattern="couple$",
    command=("couple", plugin_category),
    info={
        "header": "Just a art command try out yourself to see",
        "usage": "{tr}couple",
    },
)
async def bluedevilcouple(couple):
    "fun art command"
    await edit_or_reply(couple, H)


@catub.cat_cmd(
    pattern="sup$",
    command=("sup", plugin_category),
    info={
        "header": "Just a art command try out yourself to see",
        "usage": "{tr}sup",
    },
)
async def bluedevilsupreme(supreme):
    "fun art command"
    await edit_or_reply(supreme, I)


@catub.cat_cmd(
    pattern="india$",
    command=("india", plugin_category),
    info={
        "header": "Just a art command try out yourself to see",
        "usage": "{tr}india",
    },
)
async def bluedevilindia(india):
    "fun art command"
    await edit_or_reply(india, J)


@catub.cat_cmd(
    pattern="wc$",
    command=("wc", plugin_category),
    info={
        "header": "Just a art command try out yourself to see",
        "usage": "{tr}wc",
    },
)
async def bluedevilwelcome(welcome):
    "fun art command"
    await edit_or_reply(welcome, K)


@catub.cat_cmd(
    pattern="snk$",
    command=("snk", plugin_category),
    info={
        "header": "Just a art command try out yourself to see",
        "usage": "{tr}snk",
    },
)
async def bluedevilsnake(snake):
    "fun art command"
    await edit_or_reply(snake, L)


@catub.cat_cmd(
    pattern="bye$",
    command=("bye", plugin_category),
    info={
        "header": "Just a art command try out yourself to see",
        "usage": "{tr}bye",
    },
)
async def bluedevilbye(bye):
    "fun art command"
    await edit_or_reply(bye, O)


@catub.cat_cmd(
    pattern="shitos$",
    command=("shitos", plugin_category),
    info={
        "header": "Just a art command try out yourself to see",
        "usage": "{tr}shitos",
    },
)
async def bluedevilshitos(shitos):
    "fun art command"
    await edit_or_reply(shitos, P)


@catub.cat_cmd(
    pattern="dislike$",
    command=("dislike", plugin_category),
    info={
        "header": "Just a art command try out yourself to see",
        "usage": "{tr}dislike",
    },
)
async def bluedevildislike(dislike):
    "fun art command"
    await edit_or_reply(dislike, R)

    
@catub.cat_cmd(
    pattern="lol$",
    command=("lol", plugin_category),
    info={
        "header": "For say lol",
        "usage": "{tr}lol",
    },
)
async def bluedevillol(lol):
    "fun art command"
    await edit_or_reply(lol, S)

    
@catub.cat_cmd(
    pattern="rip$",
    command=("rip", plugin_category),
    info={
        "header": "For say rip",
        "usage": "{tr}rip",
    },
)
async def bluedevilrip(rip):
    "fun art command"
    await edit_or_reply(rip, T)

    
@catub.cat_cmd(
    pattern="cesso$",
    command=("cesso", plugin_category),
    info={
        "header": "Per mandare un cesso",
        "usage": "{tr}cesso",
    },
)
async def bluedevilrip(cesso):
    "fun art command"
    await edit_or_reply(cesso, U)

    
@catub.cat_cmd(
    pattern="dev$",
    command=("dev", plugin_category),
    info={
        "header": "Per vedere chi è il Developer(di questa versione)",
        "usage": "{tr}dev",
    },
)
async def bluedevildeveloper(dev):
    "fun art command"
    await edit_or_reply(dev, V)

    
@catub.cat_cmd(
    pattern="mm$",
    command=("mm", plugin_category),
    info={
        "header": "Per avere la spiegazione dell'mm",
        "usage": "{tr}mm",
    },
)
async def bluedevilmm(mm):
    "fun art command"
    await edit_or_reply(mm, W)

    
@catub.cat_cmd(
    pattern="motivi$",
    command=("motivi", plugin_category),
    info={
        "header": "Per avere i motivi di un netban",
        "usage": "{tr}motivi",
    },
)
async def bluedevilmotivi(motivi):
    "fun art command"
    await edit_or_reply(motivi, X)

    
@catub.cat_cmd(
    pattern="porco$",
    command=("porco", plugin_category),
    info={
        "header": "Per avere un ritratto dei Federico Vaiana",
        "usage": "{tr}porco",
    },
)
async def bluedevilporco(porco):
    "fun art command"
    await edit_or_reply(porco, Y)

    
@catub.cat_cmd(
    pattern="napoli$",
    command=("napoli", plugin_category),
    info={
        "header": "Per vedere il simbolo nel Napoli",
        "usage": "{tr}napoli",
    },
)
async def bluedevilnapoli(napoli):
    "fun art command"
    await edit_or_reply(napoli, Z)
