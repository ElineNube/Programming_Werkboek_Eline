li = list()
invoer = "5-9-7-1-7-8-3-2-4-8-7-9"

for item in invoer:
    li.append(item.strip('-'))

for element in li:
    if element == '':
        li.remove(element)

li.sort()
maximaal = max(li)
minimaal = min(li)

print('Gesorteerde lijst van ints:' + ' ' + str(li))
print('Grootste getal:' + ' ' + maximaal + ' ' + 'en kleinste getal:' + ' ' + minimaal)
print('Aantal getallen:' + ' ' + str(len(li)))
