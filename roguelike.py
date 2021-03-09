import discord
import random
from varname import nameof
from misc import *
from descs import *

# todo lista:
# * - done
# statystyki bohatera
    # * podstawowe staty
    # * wyświetlanie
# generowanie poziomu:
    # * wiecej zmiennych
    # * PER ma znaczenie
# przechodzenie miedzy poziomami
# walka
    # * podstawowy system walki
        # * predkosc broni i przeciwników
        # * śmierć przeciwników
        # * randomowy rozstrzał DMG
# rozmowa
# buffy/debuffy
# uzywanie przedmiotów


# types of types
CHARACTER = -5
ENTITY = -4
ITEM = -3
AMBIENCE = -2

# types of Entities
HUMANOID = 0
RODENT = 1

# Entities
ELF = 1
DWARF = 2
HUMAN = 3
RAT = 4

# types of Ambience

# Ambience
WATER = 0
MUSHROOMS = 1
POOL_OF_WATER = 2
LAKE = 3
VINES = 4
SKELETONS = 5
MINERALS = 6
VEGETATION = 7
HOLE = 8
ROCK_SHELF = 9

# types of items
MISC = 0
MAIN_WEAPON = 1
SECONDARY_WEAPON = 2
CONSUMABLE = 3

# Items
DAGGER = 0
BOW = 1
RATION = 2
EMPTY_FLASK = 3


class GameInfo:
    state = 1


class Item:
    ID = []
    item = []
    type = []
    durability = []
    name = []
    DMG = []
    SPEED = []

    def create(item, dur, name):
        Item.ID.append(len(Item.ID))
        Item.item.append(item)
        Item.name.append(name)
        Item.durability.append(random.randint(dur, 100))
        Item.DMG.append(1)
        Item.SPEED.append(1)
        if item == DAGGER:
            Item.type.append(SECONDARY_WEAPON)
            Item.DMG[len(Item.ID) - 1] = 5
            Item.SPEED[len(Item.ID) - 1] = 1
        if item == BOW:
            Item.type.append(MAIN_WEAPON)
            Item.DMG[len(Item.ID) - 1] = 10
            Item.SPEED[len(Item.ID) - 1] = 3
        if item == RATION:
            Item.type.append(CONSUMABLE)
        if item == EMPTY_FLASK:
            Item.type.append(MISC)
        return


class Entity:
    ID = []
    type = []
    entity = []
    name = []
    HP = []
    DMG = []
    CRIT = []
    SIZE = []

    def create(entity, name):
        Entity.ID.append(len(Entity.ID))
        Entity.entity.append(entity)
        Entity.name.append(name)
        if 1 >= entity <= 3:
            Entity.type.append(HUMANOID)
        if 4 >= entity <= 4:
            Entity.type.append(RODENT)
        if entity == RAT:
            Entity.HP.append(random.randint(5, 10))
            Entity.SIZE.append(100)
            Entity.DMG.append(2)
            Entity.CRIT.append(50)

    def delete(entity):
        Entity.ID.pop(entity)
        Entity.type.pop(entity)
        Entity.entity.pop(entity)
        Entity.name.pop(entity)
        Entity.HP.pop(entity)
        Entity.DMG.pop(entity)
        Entity.CRIT.pop(entity)
        Entity.SIZE.pop(entity)


class Character:
    race = 0
    race_str = ""
    weapon1 = -1
    weapon2 = -2
    HP = 1
    STR = 0
    DEX = 0
    INT = 0
    CHR = 0
    PER = 0
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
            Character.CHR = 2
            Character.PER = 10

            Character.HP = 40
        if var == 2:
            Character.race_str = "krasnolud"
            Character.STR = 13
            Character.DEX = 5
            Character.INT = 3
            Character.CHR = 8
            Character.PER = 4

            Character.HP = 85
        if var == 3:
            Character.race_str = "czlowiek"
            Character.STR = 7
            Character.DEX = 7
            Character.INT = 7
            Character.CHR = 9
            Character.PER = 5

            Character.HP = 60
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
        await print_commands(message)
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
        Item.create(DAGGER, 100, "sztylet")
        Item.create(BOW, 100, "łuk")
        Item.create(RATION, 100, "racja żywnościowa")
        Item.create(EMPTY_FLASK, 20, "pusta butelka")

        Character.inv.append(0)
        Character.inv.append(1)
        Character.inv.append(2)
        Character.inv.append(3)
    return
    # todo: more starting eq


async def check_stats(message):
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


async def inv_print(message):
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


def room_gen():
    Room.exits = random.randint(1, 3)
    var_count = random.randint(1, 4)
    while var_count > 0:
        repeat = 0
        var = random.randrange(0, 10, 1)
        for x in Room.ambience:
            if x == var:
                repeat = 1
                var_count += 1
        if repeat == 0:
            Room.ambience.append(var)
        var_count -= 1
    Entity.create(RAT, "szczur")  # todo: delete entities after moving to another room
    Entity.create(RAT, "szczur")
    return


async def entity_env_desc(message):
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


async def room_desc(message):
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
            text += "'!lewo'"  # todo: special senses with perception
        if x == 2:
            text += "'!przod'"
        if x == 3:
            text += "'!prawo'"
    text = text + "\n```"
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


async def char_fight(message):
    # atakuj
    var = message.content.upper()
    var_txt = var[7:len(var)]
    text = ""
    if var_txt.isnumeric():
        target = int(var_txt)
        if target < len(Entity.entity):
            speed = 0
            max_speed = 0
            if Item.SPEED[Character.weapon1] > Entity.SIZE[target] / 100:
                max_speed = Item.SPEED[Character.weapon1]
            else:
                max_speed = Entity.SIZE[target] / 100
            while Entity.HP[target] > 0:
                speed += 1
                if speed >= Item.SPEED[Character.weapon1]:  # todo: handle players death, scaling weapon with skills, handle no-weapon
                    damage = Item.DMG[Character.weapon1] - random.randint(0, int(Item.DMG[Character.weapon1] / 2))
                    text = f"""```bash
    '{message.author.name}' [{Character.HP} hp], {attack_words[random.randint(0, 3)]} z {Item.name[Character.weapon1]} za {damage}.```"""
                    Entity.HP[target] -= damage
                    await message.channel.send(text)
                if speed >= Entity.SIZE[target] / 100 and Entity.HP[target] > 0:  # todo: handle crits
                    damage = Entity.DMG[target] - random.randint(0, Entity.DMG[target] / 2)
                    text = f"""```bash
    '{Entity.name[target]}' [{Entity.HP[target]} hp], {attack_words[random.randint(0, 3)]} za {damage}.```"""
                    Character.HP -= damage
                    await message.channel.send(text)
                if speed >= max_speed:
                    speed = 0
            if Entity.HP[target] <= 0:
                text = f"""```cs
    #'{Entity.name[target]}', ginie!```"""
                Entity.delete(target)
                print(f"Ilosc ent: {Entity.ID}")
                await message.channel.send(text)
    else:
        text = "Niepoprawne użycie komendy. atakuj [liczba_stworzenia]"
        await message.channel.send(text)
    return
