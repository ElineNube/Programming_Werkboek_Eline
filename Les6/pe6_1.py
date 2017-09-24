maand = int(input('Hoeveelste maand is het nu?'))

def seizoen(maand):
    if maand >=3 and maand <=5:
        print('Het is lente!')
    elif maand >=6 and maand <=8:
        print('Het is zomer!')
    elif maand >= 9 and maand <= 11:
        print('Het is herfst!')
    elif maand >= 12 or maand <=2:
        print('Het is winter!')

print(seizoen(maand))