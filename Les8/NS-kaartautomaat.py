def inlezen_beginstation():
    beginstation = input('Wat is uw beginstation?')
    if beginstation not in stations:
        print('Uw  keuze is niet geldig. Maak een nieuwe keuze:')
        uitvoer()
    return beginstation

def inlezen_eindstation(stations, beginstation):
    eindstation = input('Wat is uw eindstation?')
    if eindstation not in stations or stations.index(eindstation) <= stations.index(beginstation):
        print('Uw  keuze is niet geldig. Maak een nieuwe keuze:')
        uitvoer()
    return eindstation

def inlezen_tussenliggende_stations(beginstation, eindstation, stations):
    indexBeginStation = stations.index(beginstation)+1
    indexEindstation = stations.index(eindstation)
    while indexBeginStation < indexEindstation:
        print('-' + stations[indexBeginStation])
        indexBeginStation += 1


def omroepen_reis(stations, beginstation, eindstation):
    prijsPerStation = 5
    nummerBeginStation = str(int(stations.index(beginstation)) + 1)
    nummerEindstation = str(int(stations.index(eindstation)) + 1)
    verschilTussenStations = str(int(nummerEindstation) - int(nummerBeginStation))
    prijsKaartje = str(int(verschilTussenStations) * prijsPerStation)
    print('\n'
          'Het beginstation ' + beginstation + ' is het ' + nummerBeginStation + 'e '  + 'station in het traject.\n' 
          'Het eindstation ' + eindstation + ' is het ' + nummerEindstation + 'e ' + 'station in het traject.\n'
          'De afstand bedraagt ' + verschilTussenStations + ' station(s).\n'
          'De prijs van het kaartje is ' + prijsKaartje + ' euro.'
          '\n'
          'Jij stapt in de trein in: ' +  beginstation + '.\n')
    inlezen_tussenliggende_stations(beginstation,eindstation,stations)
    print('\nJij stapt uit de trein in ' + eindstation + '.\n')

def uitvoer():
    while True:
        beginstation = inlezen_beginstation()
        eindstation = inlezen_eindstation(stations, beginstation)
        omroepen = omroepen_reis(stations, beginstation, eindstation)

stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'Amsterdam Centraal', 'Amsterdam Amstel', 'Utrecht Centraal',  "'s-Hertogenbosch", 'Eindhoven', 'Weert', 'Roermond', 'Sittard', 'Maastricht']
uitvoer()