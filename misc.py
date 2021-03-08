def make_spaces(max_len, txt):
    txt = str(txt)
    var = max_len - len(txt)
    i = 0
    while i < var:
        txt = txt + " "
        i += 1
    return txt


async def print_commands(message):
    text = """```bash
    'inv' lub 'ekw' (otwórz ekwipunek)
    'uzyj' [przedmiot]
    'sprawdz' [element otoczenia]
    'zaloz' [przedmiot]
    'atakuj' [cel]
    'bron' (sprawdź jaką trzymasz broń)
    'otoczenie' lub '!env' (ponownie sprawdź otoczenie)
    ```"""
    await message.channel.send(text)
    return