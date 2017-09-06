cijferICOR = 7
cijferPROG = 6
cijferCSN = 8
gemiddelde = (cijferICOR + cijferPROG + cijferCSN) / 2
beloning = (cijferICOR + cijferPROG + cijferCSN) * 30
overzicht = 'Mijn cijfers (gemiddeld een' + ' ' + str(gemiddelde)  + ') leveren een beloning van' + ' ' + str(beloning) + ' ' + 'op!'

print(overzicht)
