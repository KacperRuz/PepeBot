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

        Character.inv.append(0)
        Character.inv.append(1)
        Character.inv.append(2)
        Character.inv.append(3)
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
