from globals import *


async def room_move(message):
    from roguelike import Room
    from roguelike import Entity
    from generation import room_gen
    from descriptions import room_desc
    var = message.content.upper()
    allow = 0
    if var == "LEWO" and Room.exits >= 1:
        allow = 1
    if var == "PRZOD" and Room.exits >= 2:
        allow = 1
    if var == "PRAWO" and Room.exits == 3:
        allow = 1

    if allow == 1:
        Room.cleanup()
        Entity.cleanup()
        room_gen()
        text = f"""```Pomyślnie poszedłeś w {var}.```"""
        await message.channel.send(text)
        await room_desc(message)
    else:
        text = """```Niestety nie ma tam przejścia.```"""
        await message.channel.send(text)
    return
