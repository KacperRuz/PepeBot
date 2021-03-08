import discord
import random
from keepalive import keep_alive
from datetime import datetime
from roguelike import *

client = discord.Client()


async def czas(message):
    now = datetime.now()
    hour = now.strftime("%H")
    hour = int(hour) + 1
    hour = str(hour)
    now_str = now.strftime("Jest " + hour + ":%M\nA u Maliny jest %H:%M")
    await message.channel.send(now_str)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("<:pepeCute:809054378878435358>"):
        await message.channel.send("<:pepeCute:809054378878435358>")

    if 'WOJSKU' in message.content.upper():
        await message.channel.send("https://www.youtube.com/watch?v=3aiRv9kvf54")

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

    if message.content.startswith("!time"):
        await czas(message)
    if message.content.startswith("!quote"):
        var = random.randrange(0, 15, 1)
        if var == 0:
            await message.channel.send("> Stop! Ktoś chce zgubić wszystko. ~ Yuri <3")
        if var == 1:
            await message.channel.send("> Tak. To błąd u Pana. ~ Yuri <3")
        if var == 2:
            await message.channel.send("> Co takie śmieszne jest Polkowski? ~ Yuri <3")
        if var == 3:
            await message.channel.send("> Plus dla wszystkich! ~ Yuri <3")
        if var == 4:
            await message.channel.send("> Pan tego nie pisze 1000 razy bo my nie jestesmy w szkole. ~ Ihor")
        if var == 5:
            await message.channel.send("> Przecież to jest wiedza elementarna. ~ Ihor")
        if var == 6:
            await message.channel.send("> Chętni? ~ Ihor")
        if var == 7:
            await message.channel.send("> No ale to to głowie to można policzyć. ~ Ihor")
        if var == 8:
            await message.channel.send("> KUUURDE JAK MNIE TO DENERWUJE ~ Mariuszek")
        if var == 9:
            await message.channel.send("> Ej chlopaki bylem w lazience co sie działo? ~ Ścipior")
        if var == 10:
            await message.channel.send("> O to wam opowiem jak raz mnie policja... ~ Malina")
        if var == 11:
            await message.channel.send("> Kurwa znowu sie spóźniłem do pracy ~ Kacper")
        if var == 12:
            await message.channel.send("> To ja ide spać ~ Kacper")
        if var == 13:
            await message.channel.send("> Szybko zbranduje... ~ Marcinos")
        if var == 14:
            await message.channel.send("> WRWRWRWRWRWRWRWRWRWRWR *vietnam intesifies* ~ Wiatrowski")
    if message.content.startswith("!corobisz"):
        await message.channel.send("> !quote\n> !time\n> !randompepe\n> <:pepeCute:809054378878435358>")
    if message.content.startswith("🍌"):
        await message.channel.send("https://i.redd.it/7ewjm3w78zy41.jpg")
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
    if message.content.startswith("otoczenie") and GameInfo.state == 3 or message.content.startswith("!env") and GameInfo.state == 3:
        await room_desc(message)
    if message.content.startswith("komendy") and GameInfo.state == 3:
        await print_commands(message)





keep_alive()
client.run('ODE1MjQwMjM5MzgyNzkwMTk2.YDphow.Mnxfv3AmgcKeH-CjWla7MrFgWGw')
