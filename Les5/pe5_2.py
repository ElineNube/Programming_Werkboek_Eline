li = list()
infile = open('C:/Users/eline/OneDrive/Documenten/School/Programming/kaartnummers.txt','r')

for line in infile:
    li.append(line.strip('\n').split(','))

print(li[0][1] + ' ' + 'heeft kaartnummer:' + ' ' + li[0][0])
print(li[1][1] + ' ' + 'heeft kaartnummer:' + ' ' + li[1][0])
print(li[2][1] + ' ' + 'heeft kaartnummer:' + ' ' + li[2][0])
print(li[3][1] + ' ' + 'heeft kaartnummer:' + ' ' + li[3][0])
print(li[4][1] + ' ' + 'heeft kaartnummer:' + ' ' + li[4][0])
print(li[5][1] + ' ' + 'heeft kaartnummer:' + ' ' + li[5][0])