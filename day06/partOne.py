input = open("input.txt", "r")
total = 0
data=''
for line in input:
    if len(line)>1:
        data += line.strip()
    else: data+=line
data = data.split('\n')
for record in data:
    total+=len(set(record))
print(total)
