invoer = input('Vul een zin in:')

def gemiddelde(invoer):
    zin = invoer.split()
    res = sum(len(losWoord) for losWoord in zin) / len(zin)
    return res

print(gemiddelde(invoer))