afstandKM = int(input('Hoeveel km is er gereisd?'))
if afstandKM < 0:
    afstandKM = 0
leeftijd = int(input('Wat is je leeftijd?'))
weekendrit = str(input('Heb je in het weekend gereisd? (ja/nee)'))

def standaardprijs(afstandKM):
    prijsPerKM = 0.8
    minimaalKMMetKorting = 50
    afstandskortingBedrag = 15
    afstandskortingPerKM = 0.6
    if afstandKM > minimaalKMMetKorting:
        return afstandskortingBedrag + (afstandKM * afstandskortingPerKM)
    else:
        return afstandKM * prijsPerKM


def ritprijs(leeftijd, weekendrit, afstandKM):
    rechtOpWeekendKorting = weekendrit == 'ja'
    rechtOpLeeftijdskorting = leeftijd < 12 or leeftijd > 64
    kortingspercentageWeekend = 0.6
    kortingspercentageLeeftijd = 0.7
    kortingspercentageBeide = 0.65
    if rechtOpWeekendKorting:
        if rechtOpLeeftijdskorting:
            return standaardprijs(afstandKM) * kortingspercentageBeide
        else:
            return standaardprijs(afstandKM) * kortingspercentageWeekend
    else:
        if rechtOpLeeftijdskorting:
            return standaardprijs(afstandKM) * kortingspercentageLeeftijd
        else:
            return standaardprijs(afstandKM)

print(ritprijs(leeftijd, weekendrit, afstandKM))