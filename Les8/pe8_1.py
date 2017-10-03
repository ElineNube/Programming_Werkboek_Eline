bruin = {'Boxtel','Best','Beukenlaan','Eindhoven','Helmond t Hout','Helmond Brouwhuis','Deurne'}
groen = {'Boxtel','Best','Beukenlaan','Eindhoven','Geldrop','Heeze','Weert'}

overeenkomst = bruin.intersection(groen)
print(overeenkomst)

verschil = bruin.difference(groen)
print(verschil)