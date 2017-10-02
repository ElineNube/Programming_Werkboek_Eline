dict = {}
def namen():
    # naam = '-'
    naam = input('Volgende naam:')
    if naam != '':
        if naam in dict:
            dict[naam] += 1
        else:
            (key,val) = (naam, 1)
            dict[naam] = val
    if naam == '':
        for naam in dict:
            print('Er zijn' + ' ' + str(dict[naam]) + ' ' + 'studenten met de naam' + ' ' + str(naam))
        return;
    else:
        namen()



namen()