def convert(gradenCelsius):
    res = gradenCelsius * 1.8 + 32
    return res

def table():
    formatStr = '{:5}    {:5}'
    print(formatStr.format('C','F'))
    for gradenCelsius in range(-30,40,10):
        print(formatStr.format(gradenCelsius, convert(gradenCelsius)))

print(table())



