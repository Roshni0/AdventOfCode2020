import re
input = open('input.txt')
bus = input.read().split('\n')
bus[1] = bus[1].split(',')
arrive = int(bus[0])
buses = bus[1]
def find_multiples(input,variable):
  multiples=[]
  for i in range(input//variable+1, input//variable+2):
    multiples.append(i*variable)
  return multiples
departure={}          
for x in buses:
  if (''.join(re.findall('[0-9]', x))) != '':
    departure.update({x:find_multiples(arrive,int(x))}) 
a = int(min(departure, key=departure.get))
b = min(departure.values())[0]    
print('Part 1: ', (b-arrive)*a)

#Answer: 3882
