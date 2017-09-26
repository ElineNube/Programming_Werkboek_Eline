kluizenBestand = open('kluizen.txt', 'r')
bestand = kluizenBestand.read().splitlines()
kluizenBestand.close

#menu
print('Kies één van de volgende opties:\n'
      '1: Ik wil weten hoeveel kluizen nog vrij zijn\n'
      '2: Ik wil een nieuwe kluis\n'
      '3: Ik wil even iets uit mijn kluis halen\n'
      '4: Ik geef mijn kluis terug\n'
      '\n')
keuze = int(input('Geef uw optie:'))
if keuze < 1 or keuze >4:
        print('Maak een geldige keuze.')

#Keuze 1
def toon_aantal_kluizen_vrij():
    totaalAantalKluizen = 12
    res = totaalAantalKluizen - (len(bestand))
    return res

#Keuze 2
def nieuwe_kluis():
    maximaalKluizen = 12
    kluizenLijst = list(range(1, maximaalKluizen + 1))
    if toon_aantal_kluizen_vrij() <= 0:
        print("Er zijn geen kluizen vrij.")

    if toon_aantal_kluizen_vrij() > 0:
        for kluis in bestand:
            kluizenLijst.remove(int(kluis.split(';')[0]));
        nieuwe_kluis = kluizenLijst[0]
        print("Kluisnummer " + str(nieuwe_kluis) + " is voor jou gekozen.")
        wachtwoord = input("Kies een wachtwoord: ")
        bestand.append(str(nieuwe_kluis) + ';' + str(wachtwoord))
        save(bestand)
#Keuze 3
def kluis_format(kluisnummer, wachtwoord):
    return str(kluisnummer) + ";" + str(wachtwoord)

def open_kluis():
    kluisnummer = input("Kies jouw kluisnummer: ")
    wachtwoord = input("Kies jouw wachtwoord: ")
    for kluis in bestand:
        if kluis_format(kluisnummer, wachtwoord) == kluis:
            print("Je kluis is nu open!")
            return

    print("Je wachtwoord/kluisnummer is niet juist.")

#Keuze 4
def kluis_teruggeven():
    kluisnummer = input("Kies jouw kluisnummer: ")
    wachtwoord = input("Kies jouw wachtwoord: ")
    for kluis in bestand:
        if kluis_format(kluisnummer, wachtwoord) == kluis:
            bestand.remove(kluis)
            save(bestand)

    print("Je wachtwoord/kluisnummer is niet juist.")

#bestand overschrijven
def save(bestand):
    kluizenBestand = open("kluizen.txt","w")
    for line in bestand:
        kluizenBestand.write(line)
        kluizenBestand.write('\n')

    kluizenBestand.close()

#Functie is gekozen
if keuze == 1:
    print('Aantal kluizen vrij:' + ' ' + str(toon_aantal_kluizen_vrij()))

if keuze == 2:
    nieuwe_kluis()

if keuze == 3:
    open_kluis()

if keuze == 4:
    kluis_teruggeven()