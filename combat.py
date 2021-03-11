import random
from globals import *


def calculate_speed(wpn_speed, entity_speed):
    max_speed = 1
    if wpn_speed > entity_speed / 100:
        max_speed = wpn_speed
    else:
        max_speed = entity_speed / 100

    return max_speed


async def char_fight(message):
    from roguelike import Entity
    from roguelike import Item
    from roguelike import Character
    from descs import attack_words

    # atakuj
    var = message.content.upper()
    var_txt = var[7:len(var)]
    text = ""
    if var_txt.isnumeric():
        target = int(var_txt)
        if target < len(Entity.entity):
            speed = 0
            max_speed = 0
            is_unarmed = 0
            wpn = -1
            if Character.weapon1 < 0 and Character.weapon2 < 0:
                is_unarmed = 1
                Item.create(EMPTY_FLASK, 100, "pięści")
                Character.weapon1 = len(Item.item) - 1
                wpn = Character.weapon1
            if Character.weapon2 > -1 and Character.weapon1 == -1:
                wpn = Character.weapon2
            else:
                wpn = Character.weapon1

            max_speed = calculate_speed(Item.SPEED[wpn], Entity.SIZE[target])

            while Entity.HP[target] > 0:  # main combat loop
                speed += 1

                # Using additional weapon (left hand)
                if Character.weapon2 > -1:
                    if Entity.HP[target] < Item.DMG[Character.weapon2]:
                        wpn = Character.weapon2
                        max_speed = calculate_speed(Item.DMG[wpn], Entity.SIZE[target])

                # Player strike
                if speed >= Item.SPEED[wpn]:  # todo: handle players death, scaling weapon with skills, handle no-weapon, handle 2nd weapon
                    damage = Item.DMG[wpn] - random.randint(0, int(Item.DMG[wpn] / 2))
                    text = f"""```bash
    '{message.author.name}' [{Character.HP} hp], {attack_words[random.randint(0, len(attack_words) - 1)]} '{Entity.name[target]}' z {Item.name[wpn]} za {damage}.```"""
                    Entity.HP[target] -= damage
                    await message.channel.send(text)

                # Entity strike
                if speed >= Entity.SIZE[target] / 100 and Entity.HP[target] > 0:  # todo: handle crits
                    damage = Entity.DMG[target] - random.randint(0, Entity.DMG[target] / 2)
                    text = f"""```bash
    '{Entity.name[target]}' [{Entity.HP[target]} hp], {attack_words[random.randint(0, len(attack_words) - 1)]} '{message.author.name}' za {damage}."""
                    if random.randint(0, 100) <= Item.SPEED[Character.armor]:
                        block = Item.DMG[Character.armor] - random.randint(0, int(Item.DMG[Character.armor] / 2))
                        if damage - block < 0:
                            block = damage
                            damage = 0
                        text += f" '{message.author.name}' blokuje {block} obrażeń.```"
                    else:
                        text += "```"
                    Character.HP -= damage
                    await message.channel.send(text)
                if speed >= max_speed:
                    speed = 0

            # Entity death
            if Entity.HP[target] <= 0:
                text = f"""```cs
    #{Entity.name[target]}, ginie!```"""
                Entity.delete(target)
                if is_unarmed == 1:
                    Item.delete(Character.weapon1)
                    Character.weapon1 = -1
                print(f"Ilosc ent: {Entity.ID}")
                await message.channel.send(text)
    else:
        text = "Niepoprawne użycie komendy. atakuj [liczba_stworzenia]"
        await message.channel.send(text)
    return