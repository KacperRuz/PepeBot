from globals import *


async def inv_print(message):
    from roguelike import Character
    from roguelike import Item
    from misc import make_spaces
    text = """```asciidoc
"""
    if len(Character.inv) > 0:
        for x in range(0, len(Character.inv)):
            text_it: str = "[" + str(x) + "]"
            text_it += Item.name[x]
            text_it = make_spaces(32, text_it)
            text += text_it + str(Item.durability[x]) + "%"
            if x == Character.weapon1:
                text += " [prawa ręka]"
            if x == Character.weapon2:
                text += " [lewa ręka]"
            text += "\n"
        text = text + "\n```"
    else:
        text += "Twój ekwipunek jest kompletnie pusty!```"
    await message.channel.send(text)
    return


async def equip_weapon(message):
    from roguelike import Item
    from roguelike import Character
    var = message.content.upper()
    # zaloz
    it_id = var[6:len(var)]
    text = ""
    print(it_id)
    if len(it_id) > 0:
        if it_id.isnumeric():
            it_id = int(it_id)

            if it_id <= len(Item.ID) - 1:
                print(it_id)
                if Item.type[it_id] == MAIN_WEAPON:
                    Character.weapon1 = it_id
                    text += "Wziąłeś " + str(Item.name[it_id]) + " do prawej ręki."
                else:
                    Character.weapon2 = it_id
                    text += "Wziąłeś " + str(Item.name[it_id]) + " do lewej ręki."
            else:
                text += "Nie ma takiego przedmiotu."
        else:
            text += "Niepoprawne użycie komendy. zaloz [liczba_przedmiotu_w_inv]"
    else:
        text += "Nie ma takiego przedmiotu."
    await message.channel.send(text)
    return


async def check_weapon(message):
    from roguelike import Character
    from roguelike import Item
    from misc import make_spaces
    text = """```bash
(prawa ręka): """
    text_wpn1 = ""
    text_wpn2 = ""
    if Character.weapon1 > -1:
        text_wpn1 = str(Item.name[Character.weapon1])
        make_spaces(32, text_wpn1)
    text += text_wpn1 + "\n(lewa reka): "
    if Character.weapon2 > -1:
        text_wpn2 = str(Item.name[Character.weapon2])
        make_spaces(32, text_wpn2)
    text += text_wpn2 + "\n```"

    await message.channel.send(text)
    return
