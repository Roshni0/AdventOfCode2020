preamble_size = 25
preamble = None
inputs = None
nums = None
with open('input.txt') as f:
    nums = list(map(lambda x: int(x), f.read().split("\n")))
    preamble = nums[0:preamble_size]
    inputs = nums[preamble_size:]
illegal = None
for input in inputs:
    found = False
    for num in preamble:
        if (input - num) in preamble and (input - num ) != num:
            found = True
    if not found:
        illegal = input
        break
    preamble.append(input)
    preamble = preamble[1:]
print(illegal)

#Answer: 41682220
