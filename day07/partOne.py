def get_input() -> list:
    with open(r'input.txt', 'r') as file:
        file_list = file.read().splitlines()
    return file_list

def part_one(bag_list:list, looking_for:str) -> list:
    found_list = []
    for bag in bag_list:
        sep = bag.find(' bags contain')
        if looking_for in bag[sep:]:
            found_list.append(bag[:sep])
            found_list.extend(part_one(bag_list, bag[:sep]))
    return found_list
print(f'\nDAY 07 Part 1:  The shiny gold bag can go in {len(set(part_one(get_input(), "shiny gold")))} bags.')
