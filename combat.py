import random


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
            if Item.SPEED[Character.weapon1] > Entity.SIZE[target] / 100:
                max_speed = Item.SPEED[Character.weapon1]
            else:
                max_speed = Entity.SIZE[target] / 100
            while Entity.HP[target] > 0:
                speed += 1
                if speed >= Item.SPEED[Character.weapon1]:  # todo: handle players death, scaling weapon with skills, handle no-weapon, handle 2nd weapon
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