numLines = 0
li = list()
infile = open('C:/Users/eline/OneDrive/Documenten/School/Programming/kaartnummers.txt','r')

for line in infile:
    li.append(line.strip('\n').split(','))
    numLines += 1

print('Deze file telt' + ' ' + str(numLines) + ' ' + 'regels')
print('Het grootste kaartnummer is:' + ' ' + max(li[3]))