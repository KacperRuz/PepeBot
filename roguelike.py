import discord
import random
from misc import *

ELF = 1
DWARF = 2
HUMAN = 3

WATER = 0
MUSHROOMS = 1

DAGGER = 0
BOW = 1
RATION = 2
EMPTY_FLASK = 3


class GameInfo:
    state = 1


class Item:
    ID = []
    type = []
    durability = []
    name = []

    def create(type, dur, name):
        Item.ID.append(len(Item.ID))
        Item.type.append(type)
        Item.durability.append(random.randint(dur, 100))
        Item.name.append(name)
        return


class Character:
    race = 0
    race_str = ""
    weapon1 = -1
    weapon2 = -2
    STR = 0
    DEX = 0
    INT = 0
    inv = []


class Room:
    exits = 0
    entities = []
    objects = []
    ambience = []


async def rog_cancel(message):
    text = ""
    if GameInfo.state == 0:
        text = """```bash
Jeszcze nie zacząłeś a już się poddajesz? Nie bój się to nie urząd miasta!
```
"""
    if GameInfo.state == 1:
        GameInfo.state = 0
        text = """```bash
Przykro mi to słyszeć... Ale będę tu na Ciebie czekał, wierzę, że jeszcze odnajdziesz scieżkę bohatera!
```
"""
    await message.channel.send(text)
    return


async def rog_start(message):
    if GameInfo.state == 1:
        wrong_message_text = """```bash
Niestety brak umiejętności czytania ze zrozumieniem, może być sporym problemem podczas zdobywania tytułu bohatera...
Wpisz '!anuluj' aby zrezygnować z przygody, lub '!start' aby wyruszyć ku wiecznej chwale!
```
"""
        await message.channel.send(wrong_message_text)
    if GameInfo.state == 0:
        GameInfo.state = 1
        welcome_text1 = "Witaj w żabim rogalu wędrowcze! <:peepoGlad:817758029159202816>"
        welcome_text2 = """```bash
Na swej drodzę do chałwy i pięknych dziewczyn napotkasz wiele niebezpieczeństw! Wygłodniałe płazy, uszczelki pod głowicą, ukraincy...
A to dopiero początek!
Więc może odpocznij jeszcze w pobliżu ciepłego żaru ogniska? 🔥 Wpisz '!anuluj' aby porzucić przygodę i wrócić do codziennej nudy.
Jeśli jednak jesteś gotów wyruszyć w nieznane, zbierz swoją drużynę do kupy i wpisz '!start' aby rozpocząć!
```
"""
        await message.channel.send(welcome_text1)
        await message.channel.send(welcome_text2)
    return


async def choose_character(var, message):
    var = int(var)
    if var >= 1 and var <= 3:
        GameInfo.state = 3
        Character.race = var
        if var == 1:
            Character.race_str = "elf"
            Character.STR = 4
            Character.DEX = 10
            Character.INT = 7
        if var == 2:
            Character.race_str = "krasnolud"
            Character.STR = 13
            Character.DEX = 5
            Character.INT = 3
        if var == 3:
            Character.race_str = "czlowiek"
            Character.STR = 7
            Character.DEX = 7
            Character.INT = 7
        welcome_text = f"""```bash
A więc '{Character.race_str}'!
Ruszajmy! Nie ma czasu do stracenia!
====================================
Wraz ze swoją ekipą wyruszacie w podróż. Zapasy są skromne, a powóz niewielki, ale za to morale dopisują każdemu jednemu.
Mijają dni, piękna pogoda, zapierające dech w piersiach widoki dawno nie czułeś takiej bliskości z naturą.
Czujesz się jak nowo narodzony, aż tu nagle...
$JEB* $JEB* $JEBUDU*
Jedno z kół w waszym wozie przemieniło się w kupkę drzazg. Można sobie zadać pytanie: kto kierowcą kurwa był?
Utknęliście, jedynym waszym schronieniem jest niewielka jaskinia w zboczu góry. Wygląda podejrzanie, a to jest roguelike fantasy RPG...
===================================
Gdy tylko stawiasz pierwsze kilka kroków w ciemność, potykasz się o delikatną linkę na wysokość kostek.
$sssssssssssssssstt*
Słysysz jak uwalniany jest jakiś mechanizm, rozglądasz się gwałtownie i rzucasz ku wyjściu...
$HHRRRRRRRRRRRRRDUUUUUUUT*
Za późno... wejście zostało zasypane. Przerażony próbujesz prędko odgarnąć kilka skał niestety na próżno.
Pomieszczenia zaczyna wypełniać się nieprzyjemnym zapachem, kaszlesz ociężale, to musi być gaz pewnego sortu.
Nie masz przy sobię nic poza podstawowym ekwipunkiem i małym posiłkiem. Misja ratunkowa może zająć dni, a nawet tygodnie, nie masz wątpliwości -
musisz iść w głąb jaskini i znaleźć inne wyjście, inaczej nie przetrwasz. Nie patrz za siebie! 
====================================
komendy:
'inv' lub 'ekw' (otwórz ekwipunek)
'uzyj' [przedmiot]
'sprawdz' [element otoczenia]
'zaloz' [przedmiot]
'atakuj' [cel]
'bron' (sprawdź jaką trzymasz broń)
'otoczenie' lub 'env' (ponownie sprawdź otoczenie)
'komendy' (lista poleceń)
```
"""
    else:
        welcome_text = """```bash
Niestety nie ma takiej postaci do wyboru.
"""
    await message.channel.send(welcome_text)

    if Character.race > 0:
        inv_gen()
        room_gen()
        await room_desc(message)
        return

    return


async def rog_begin(message):
    GameInfo.state = 2
    begin_text = f"""```bash
Witaj '{message.author.name}'!
Jaką postać tym razem wybierzesz? Pamiętaj, każda ma swoje plusy dodatnie i plusy ujemne!
'(1)Elf' sprytnie uniknie lecącą w niego strzałę lecz ciężki głaz stojący na jego drodzę będzie dużym wyzwaniem!
'(2)Krasnolud' owy głaz rozłupie bez wysiłku przy użyciu kilofa, za to będzie zbyt wolny aby w porę ukryć się przed spadającym z góry odłamkiem skalnym.
'(3)Człowiek' po wielu godzinach pokona głaz, możliwe, że uniknie też kilka nagłych niespodzianek... można śmialo powiedzieć, że jest średni!

Gdy już podejmiesz decyzję, wpisz 'odpowiednią cyfrę' w polu tekstowym.
```
"""
    await message.channel.send(begin_text)
    return


def inv_gen():
    if Character.race == ELF:
        Item.create(DAGGER, 100, "/ sztylet")
        Item.create(BOW, 100, ") łuk")
        Item.create(RATION, 100, "% racja żywnościowa")
        Item.create(EMPTY_FLASK, 20, "# pusta fiolka")

        Character.inv.append(0)
        Character.inv.append(1)
        Character.inv.append(2)
        Character.inv.append(3)
    return
    # todo: more starting eq


async def check_weapon(message):
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


async def equip_weapon(message):
    var = message.content.upper()
    # zaloz
    it_id = var[5:7]  # todo: probably need to expand for 2 digits things in future
    text = ""
    if len(it_id) > 0:
        it_id = int(it_id)
        if it_id <= len(Item.ID) - 1:
            print(it_id)
            Character.weapon1 = it_id  # todo: make usable for shields in future(add real types to items)
            text += "Wziąłeś " + str(Item.name[it_id]) + " do prawej ręki."
        else:
            text += "Nie ma takiego przedmiotu."
    else:
        text += "Nie ma takiego przedmiotu."
    await message.channel.send(text)
    return


async def inv_print(message):
    text = """```asciidoc
"""
    if len(Character.inv) > 0:
        for x in Character.inv:
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


def room_gen():
    Room.exits = random.randint(1, 3)
    var = random.randrange(0, 2, 1)
    Room.ambience.append(var)
    return


async def room_desc(message):
    text = """```bash
"""
    for x in Room.ambience:
        if x == WATER:
            text = text + "Czujesz 'wodę' pod stopami.\n"
        if x == MUSHROOMS:  # todo: seeing special ambience with dex
            text = text + "Widzisz w okolicy kilka 'grzybów'.\n"
    text = text + "Mozliwe drogi to: "
    for x in range(1, Room.exits + 1, 1):
        if x == 1:
            text = text + "'!lewo'"  # todo: special senses with dex
        if x == 2:
            text = text + "'!przod'"
        if x == 3:
            text = text + "'!prawo'"
    text = text + "\n```"
    await message.channel.send(text)

    return
