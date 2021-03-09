def make_spaces(max_len, txt):
    txt = str(txt)
    var = max_len - len(txt)
    i = 0
    while i < var:
        txt = txt + " "
        i += 1
    return txt


def replace_polish_chars(var):
    var = var.replace('ż', "z")
    var = var.replace('ź', "z")
    var = var.replace('ł', "l")
    var = var.replace('ę', "e")
    var = var.replace('ą', "a")
    var = var.replace('ó', "o")
    var = var.replace('ń', "n")
    var = var.replace('ć', "c")
    var = var.replace('ś', "s")
    return var


async def print_commands(message):
    text = """```bash
'inv' lub 'ekw' (otwórz ekwipunek)
'uzyj' [przedmiot]
'sprawdz' [element otoczenia]
'zaloz' [przedmiot]
'atakuj' [cel]
'bron' (sprawdź jaką trzymasz broń)
'otoczenie' lub 'env' (ponownie sprawdź otoczenie)
```"""
    await message.channel.send(text)
    return