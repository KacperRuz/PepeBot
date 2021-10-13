import discord
import random
from keepalive import keep_alive
from datetime import datetime

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    from roguelike import GameInfo
    from roguelike import rog_start
    from roguelike import rog_cancel
    from roguelike import rog_begin
    from roguelike import choose_character
    from inventory import inv_print
    from inventory import check_weapon
    from inventory import equip_weapon
    from descriptions import room_desc
    from descriptions import check_stats
    from descriptions import entity_env_desc
    from misc import print_commands
    from combat import char_fight
    from exploration import room_move
    if message.author == client.user:
        return

    if message.content.startswith("<:pepeCute:809054378878435358>"):
        await message.channel.send("<:pepeCute:809054378878435358>")

    if message.content.startswith("!randompepe"):
        var = random.randrange(0, 4, 1)
        if var == 0:
            await message.channel.send("<:pepeCute:809054378878435358>")
        if var == 1:
            await message.channel.send("<:Sadge:809054899736018974>")
        if var == 2:
            await message.channel.send("<:peepoSad:809054869985034240>")
        if var == 3:
            await message.channel.send("<:peepoFat:808066098519212042>")
            
    if message.content.startswith("!corobisz"):
        await message.channel.send("> !quote\n> !time\n> !randompepe\n> <:pepeCute:809054378878435358>")
    if message.content.startswith("!roguelike") and GameInfo.state == 0 or message.content.startswith("!roguelike") and GameInfo.state == 1:
        await rog_start(message)
    if message.content.startswith("!anuluj") and GameInfo.state == 0 or message.content.startswith("!anuluj") and GameInfo.state == 1:
        await rog_cancel(message)
    if GameInfo.state == 2 and message.content.upper() != "!start":
        print(message.content.upper())
        await choose_character(message.content.upper(), message)
    if message.content.startswith("!start") and GameInfo.state == 1:
        await rog_begin(message)
    if message.content.startswith("inv") and GameInfo.state == 3 or message.content.startswith("ekw") and GameInfo.state == 3:
        await inv_print(message)
    if message.content.startswith("bron") and GameInfo.state == 3:
        await check_weapon(message)
    if message.content.startswith("zaloz") and GameInfo.state == 3:
        await equip_weapon(message)
    if message.content.startswith("otoczenie") and GameInfo.state == 3 or message.content.startswith("env") and GameInfo.state == 3:
        await room_desc(message)
    if message.content.startswith("komendy") and GameInfo.state == 3:
        await print_commands(message)
    if message.content.startswith("sprawdz") and GameInfo.state == 3:
        await entity_env_desc(message)
    if message.content.startswith("stats") and GameInfo.state == 3:
        await check_stats(message)
    if message.content.startswith("atakuj") and GameInfo.state == 3:
        await char_fight(message)
    if message.content.startswith("lewo") or message.content.startswith("przod") or message.content.startswith("prawo"):
        if GameInfo.state == 3:
            await room_move(message)






keep_alive()
client.run('')
