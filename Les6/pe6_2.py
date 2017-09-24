ingegevenLijst = eval(input('Geef me een lijst van minimaal 10 woorden:'))
list = []

for string in ingegevenLijst:
    if len(string) == 4:
        list.append(string)

print(list)