studentencijfers = [ [95, 92, 86],[66, 75, 54],[89, 72, 100],[34, 0, 0] ] 

def gemiddelde_per_student(studentencijfers): 
    gemiddeldes = []
    for student in studentencijfers:
        gemiddeldes.append(sum(student)/3)
    
    return gemiddeldes

def gemiddelde_van_alle_studenten(studentencijfers): 
    total = 0
    length = 0
    for student in studentencijfers:
        for cijfer in student:
            total += cijfer
            length += 1

    return total/length
 

print(gemiddelde_per_student(studentencijfers)) 

print(gemiddelde_van_alle_studenten(studentencijfers))

