from globals import *
import random

# starting inventory gen


def inv_gen():
    from roguelike import Character
    from roguelike import Item
    if Character.race == ELF:
        Item.create(DAGGER, 100, "sztylet")
        Item.create(BOW, 100, "łuk")
        Item.create(RATION, 100, "racja żywnościowa")
        Item.create(EMPTY_FLASK, 20, "pusta butelka")
        Item.create(ELF_ROBE, 100, "elfie odzienie")

        Character.armor = len(Item.item) - 1
        for x in range(0, len(Item.item), 1):
            Character.inv.append(range(0, len(Item.item), 1))
    return
    # todo: more starting eq


def room_gen():
    from roguelike import Entity
    from roguelike import Room
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
