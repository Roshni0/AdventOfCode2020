def generate_addresses(mask, value):
    value_binary = f"{value:36b}".replace(' ', '0')
    new_value = []
    for i in range(len(mask)):
        if mask[i] == '0':
            new_value += value_binary[i]
        else:
            new_value += mask[i]
    indeces_of_x = [idx for idx, val in enumerate(new_value) if val == 'X']
    x_count = new_value.count('X')
    for i in range(pow(2, x_count)):
        i_binary = list(f"{i:b}")
        zeroes_to_add = ['0'] * (x_count - len(i_binary))
        i_binary = zeroes_to_add + i_binary
        for iter, val in enumerate(i_binary):
            target_idx = indeces_of_x[iter]
            new_value[target_idx] = val
        yield int(''.join(new_value), 2)

def part2(program):
    mem = dict()
    current_mask = ''
    for line in program:
        key_word, para = line.split(' = ')
        if key_word == 'mask':
            current_mask = para
        else:
            para = int(para)
            write_to = int(key_word.strip('mem[]'))
            for i in generate_addresses(current_mask, write_to):
                mem[i] = para
    return sum(mem.values())

with open('input.txt', 'r') as file:
    program = file.read().splitlines()
print(part2(program))

#Answer: 3219837697833
