import re
import numpy as np
input = open('input.txt')
bus = input.read().split('\n')
bus[1] = bus[1].split(',')
arrive = int(bus[0])
buses = bus[1]
t=int(buses[0])   
step=int(buses[0])  
for x in buses[1:]:
  if (''.join(re.findall('[0-9]', x))) != '':  
    while(True):
      if (t+buses.index(x)) % int(x) == 0:  
        break;
      t += step                     
    step = np.lcm(step, int(x))
print(t)

#Answer: 867295486378319
