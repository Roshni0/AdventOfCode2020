data = set()                                                  
with open('input.txt', 'r') as f:                                               
    for line in f:                                            
        i = int(line)                                                           
        if 2020 - i in data:                                                 
            print(i*(2020 - i))                                                 
            break                                                               
        else:                                                                   
            data |= {i}
