f = open(r"input.txt", "r")
numbers = sorted([int(l.split()[0]) for l in f.readlines()])

def findDif(last_number):
    dif = []
    for n in numbers:
        dif.append(n-last_number)
        last_number = n
    dif.append(3)
    return dif
dif = findDif(0)
r1 = dif.count(1)*(dif.count(3))
print(r1)

#Answer: 2310
