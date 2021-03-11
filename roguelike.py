import discord
import random
from varname import nameof
from misc import *
from descs import *
from globals import *
from descriptions import *
from inventory import *
from generation import *
from combat import *

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
        # * zbroje
        # * walka bez broni / z dodatkową
# rozmowa
# buffy/debuffy
# uzywanie przedmiotów


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
        if item == ELF_ROBE:
            Item.type.append(ARMOR)
            Item.DMG[len(Item.ID) - 1] = 3
            Item.SPEED[len(Item.ID) - 1] = 40  # speed = chance to protect
        return

    def delete(item):
        Item.ID.pop(item)
        Item.item.pop(item)
        Item.type.pop(item)
        Item.durability.pop(item)
        Item.name.pop(item)
        Item.DMG.pop(item)
        Item.SPEED.pop(item)


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

    @staticmethod
    def cleanup():
        Entity.ID.clear()
        Entity.type.clear()
        Entity.entity.clear()
        Entity.name.clear()
        Entity.HP.clear()
        Entity.DMG.clear()
        Entity.CRIT.clear()
        Entity.SIZE.clear()


class Character:
    race = 0
    race_str = ""
    weapon1 = -1
    weapon2 = -2
    armor = -1
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

    @staticmethod
    def cleanup():
        Room.exits = 0
        Room.ambience.clear()
        return


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

