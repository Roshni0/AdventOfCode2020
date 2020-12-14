preamble_size = 25
preamble = None
inputs = None
nums = None
with open('input') as f:
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

decoded = None
for i in range(0, len(nums)):
    curr_range = [nums[i]]
    sum = nums[i]
    for j in range(i + 1, len(nums)):
       sum += nums[j]
       curr_range.append(nums[j])
       if sum == illegal:
           decoded = max(curr_range) + min(curr_range)
           break
    if decoded:
        break
print(decoded)

#Answer: 5388976
