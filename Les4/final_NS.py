#input
afstandKM = float(input('Hoeveel KM is er afgelegd?'))
if float(afstandKM) < 0:
    afstandKM = 0

leeftijd = int(input('Wat is de leeftijd?'))
weekendrit = input('Is er in het weekend gereisd? (ja/nee)')

def standaardprijs(afstandKM):
    prijsPerKM = 0.80
    minimaleAfstandVoorKorting = 50.0
    vastBedragAfstandskorting = 15
    afstandskorting = 0.6

    res = prijsPerKM * afstandKM
    if afstandKM > minimaleAfstandVoorKorting:
        res = vastBedragAfstandskorting + (afstandskorting * float(afstandKM))
    return res

def ritprijs(leeftijd, weekendrit, afstandKM):
    percentageKortingLeeftijd = 0.7
    percentageKortingWeekend = 0.6
    percentageKortingLeeftijdenWeekend = 0.65
    leeftijdsKorting = standaardprijs(afstandKM) * percentageKortingLeeftijd
    weekendKorting = standaardprijs(afstandKM) * percentageKortingWeekend
    leeftijdEnWeekendkorting = float(standaardprijs(afstandKM)) * percentageKortingLeeftijdenWeekend

    rechtOpLeeftijdskorting = leeftijd < 12 or leeftijd > 64
    rechtOpWeekendkorting = weekendrit == 'ja'
    res = standaardprijs
    if rechtOpLeeftijdskorting and rechtOpWeekendkorting:
        res = leeftijdEnWeekendkorting

    if rechtOpLeeftijdskorting:
        res = leeftijdsKorting

    if rechtOpWeekendkorting:
        res = weekendKorting
    return res

print('De standaardprijs is' + ' ' + str(standaardprijs(afstandKM)) + ' ' + 'euro.')
print('De prijs inclusief korting is' + ' ' + str(ritprijs(leeftijd, weekendrit, afstandKM)) + ' ' + 'euro.')