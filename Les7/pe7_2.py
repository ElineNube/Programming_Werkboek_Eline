def woord_programma():
    while True:
        woord = input('Geef een woord van 4 letters:')
        if len(woord) == 4:
            break
        else:
            print('Het gekozen woord heeft' + ' ' + str(len(woord)) + ' ' + 'letters.')
            continue
    print(woord + ' ' + 'is goedgekeurd.')

woord_programma()