def ticker():
    while True:
        filename = open('ticker-symbols.txt', 'r')
        dictionary = {}
        for line in filename:
            regelZonderEnter = line.replace('\n','')
            (key, val) = regelZonderEnter.split(':')
            dictionary[key] = val
        key = input('Wat is de bedrijfsnaam?')
        print(dictionary[key])

ticker()