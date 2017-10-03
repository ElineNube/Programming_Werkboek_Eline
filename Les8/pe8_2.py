import random

def monopolyworp():
    getal1 = random.randrange(1,6)
    getal2 = random.randrange(1,6)
    totaal = getal1 + getal2
    print(str(getal1) + ' ' + '+' + ' ' + str(getal2) + ' ' + '=' + ' ' + str(totaal))
    if getal1 == getal2:
        print('dubbel')
monopolyworp()
