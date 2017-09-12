def wijzig(letterlijst):
    res = letterlijst[0] = 'd'
    letterlijst[1]= 'e'
    letterlijst[2]='f'
    return res

letterlijst = ['a','b','c']
print(letterlijst)
wijzig(letterlijst)
print(letterlijst)