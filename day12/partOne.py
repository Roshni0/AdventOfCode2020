import math

with open('input.txt') as reader:
    plan = [(line[0],int(line[1:])) for line in reader]

heading = 0
east = 0
north = 0

translations = {
    'L': lambda v: ((heading + v) % 360,east,north),
    'R': lambda v: ((heading - v) % 360,east,north),
    'F': lambda v: (heading, round(east + math.cos((heading/90)*(math.pi/2))*v), round(north + math.sin((heading/90)*(math.pi/2))*v)),
    'N': lambda v: (heading, east, north + v),
    'S': lambda v: (heading, east, north - v),
    'E': lambda v: (heading, east + v, north),
    'W': lambda v: (heading, east - v, north)
}
for move in plan:
    (heading,east,north) = translations[move[0]](move[1])
print(abs(north) + abs(east))

#Answer: 2228
