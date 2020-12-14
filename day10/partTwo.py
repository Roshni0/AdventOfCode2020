f = open(r"input.txt", "r")
numbers = sorted([int(l.split()[0]) for l in f.readlines()])

def findDif(last_number):
    dif = []
    for n in numbers:
        dif.append(n-last_number)
        last_number = n
    dif.append(3)
    return dif

def findArrs(dif):
    temp_list = []
    mult_list = []
    for n in dif:
        if n != 3:
            temp_list.append(n)
        
        elif n == 3:
            if len(temp_list) > 3:
                mult_list.append((len(temp_list)-1)*2+(len(temp_list)-3))
            elif len(temp_list) > 1:
                mult_list.append((len(temp_list)-1)*2)
            temp_list = []    
    r2 = 1
    for x in mult_list:
            r2 = r2 * x 
    return r2

dif = findDif(0)
print(findArrs(dif))

#Answer: 64793042714624
