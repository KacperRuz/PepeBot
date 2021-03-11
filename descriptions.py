from globals import *
from descs import *


async def check_stats(message):
    from roguelike import Character
    text = f"""```cs
'{message.author.name}' [{Character.HP} hp]
Rasa: {Character.race_str}
STR: {Character.STR}
DEX: {Character.DEX}
INT: {Character.INT}
CHR: {Character.CHR}
PER: {Character.PER}
```
"""
    await message.channel.send(text)
    return


async def room_desc(message):
    from roguelike import Room
    from roguelike import Character
    from roguelike import Entity
    from misc import make_spaces
    text = """```bash
"""
    for x in Room.ambience:
        if x == WATER:
            if Character.PER >= 1:
                text += "Czujesz 'wodę' pod stopami.\n"
        if x == MUSHROOMS:
            if Character.PER >= 4:
                text += "W niektórych miejscach rosną małe gromady 'grzybów'.\n"
        if x == POOL_OF_WATER:
            if Character.PER >= 5:
                text += "W ustronnym miejscu dostrzegasz niewielkie 'zagłębienie' wypełnione wodą.\n"
        if x == LAKE:
            if Character.PER >= 1:
                text += "W centrum znajduję się niewielkie 'jezioro'. Wydaję się być głębokie.\n"
        if x == VINES:
            if Character.PER >= 2:
                text += "Na ścianach jaskini możesz zobaczyć wijące się 'liany'.\n"
        if x == SKELETONS:
            if Character.PER >= 3:
                text += "Nieopodal leży stos bliżej nieokreślonych 'kości'.\n"
        if x == MINERALS:
            if Character.PER >= 6:
                text += "Ściany punktowo mienią się od 'minerałów'.\n"
        if x == VEGETATION:
            if Character.PER >= 4:
                text += "Niewielkie płaty gruntu są ozdobione przez niskie 'rośliny'.\n"
        if x == HOLE:
            if Character.PER >= 8:
                text += "Dostrzegasz 'zagłębienie' w skalnej podłodze.\n"
        if x == ROCK_SHELF:
            if Character.PER >= 10:
                text += "Wysoko na jednej ze ścian wyłania się skalna 'półka'.\n"
    text = text + "Możliwe drogi to: "
    for x in range(1, Room.exits + 1, 1):
        if x == 1:
            text += "'lewo'"  # todo: special senses with perception
        if x == 2:
            text += ", 'przod'"
        if x == 3:
            text += ", 'prawo'"
    text = text + ".\n```"
    await message.channel.send(text)

    if len(Entity.ID) > 0:
        text = """```cs
Postacie, które widzisz: \n
"""
        for x in range(0, len(Entity.ID)):
            print(x)
            text_ent = "[" + str(x) + "] "
            text_ent += Entity.name[x]
            text_ent = make_spaces(32, text_ent)
            text_ent += "(" + str(Entity.HP[x]) + " hp)\n"
            text += text_ent
        text += "\n```"
        await message.channel.send(text)
    return


async def entity_env_desc(message):
    from roguelike import Item
    from roguelike import Entity
    from misc import replace_polish_chars
    var = message.content.upper()
    # sprawdz
    var_txt = var[8:len(var)]
    var_txt = var_txt.lower()
    print(var_txt)
    is_in_eq = 0
    for x in Item.name:
        if x == var_txt:
            var_txt = replace_polish_chars(var_txt)
            var_txt = var_txt.replace(" ", "_")
            var_ascii = var_txt + "_ascii"
            print(var_ascii)
            await message.channel.send(globals()[var_ascii])
            var_desc = var_txt + "_desc"
            print(var_desc)
            await message.channel.send(globals()[var_desc])
            is_in_eq = 1
            break
    if is_in_eq == 0:
        for x in Entity.name:
            if x == var_txt:
                var_txt = replace_polish_chars(var_txt)
                var_txt = var_txt.replace(" ", "_")
                var_ascii = var_txt + "_ascii"
                print(var_ascii)
                await message.channel.send(globals()[var_ascii])
                var_desc = var_txt + "_desc"
                print(var_desc)
                await message.channel.send(globals()[var_desc])
                is_in_eq = 1
    if is_in_eq == 0:
        await message.channel.send("Nie ma takiego elementu otoczenia / stworzenia / przedmiotu w ekwipunku.")
    return
