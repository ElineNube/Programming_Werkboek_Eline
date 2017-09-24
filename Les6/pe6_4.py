li = list()
studentencijfers = [ [95, 92, 86],[66, 75, 54],[89, 72, 100],[34, 0, 0] ]

def gemiddelde_per_student(studentencijfers):
    res = [int(sum(studentencijfers[0])/3), int(sum(studentencijfers[1])/3), int(sum(studentencijfers[2])/3), int(sum(studentencijfers[3])/3)]
    return res

def gemiddelde_van_alle_studenten(studentencijfers):
    res = int((int(sum(studentencijfers[0])/3) + int(sum(studentencijfers[1])/3) + int(sum(studentencijfers[2])/3) + int(sum(studentencijfers[3])/3)) / 4)
    return res

print(gemiddelde_per_student(studentencijfers))
print(gemiddelde_van_alle_studenten(studentencijfers))

