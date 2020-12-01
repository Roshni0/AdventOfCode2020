import sys                                                                      
with open('input.txt', 'r') as f:                                               
    dat = {int(line) for line in f}                                         
for i in dat:                                                               
    for j in dat:                                                           
        if 2020 - i - j in dat:                                             
            print(i * (2020 - i - j) * j)                                       
            sys.exit()  
