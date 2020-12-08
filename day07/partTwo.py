def get_input() -> list:
    with open(r'input.txt', 'r') as file:
        file_list = file.read().splitlines()
    return file_list

def part_two(bag_list:dict, looking_for:str):
    bag_count = 1
    for bag_type in bag_list[looking_for]:
        bag_count += bag_type[0] * part_two(bag_list, bag_type[1])
    return bag_count

def reformat(bag_list:list):
    list_to_dict = {}
    for bag in bag_list:
        sep = bag.find(' bags contain')
        key = bag[:sep]
        contents = bag[sep + 14:]
        bag_instance = []
        if contents[-14:] != 'no other bags.':
            con_list = contents.split(' ')
            for i in range(0, len(con_list), 4):
                bag_num = int(con_list[i])
                bag_type = f'{con_list[i+1]} {con_list[i+2]}'
                bag_instance.append([bag_num, bag_type])
        list_to_dict[key] = bag_instance
    return list_to_dict

print(f'Part 2:  The shiny gold bag contains {part_two(reformat(get_input()), "shiny gold") - 1} bags.')
