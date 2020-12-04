import re

def get_data():
  with open("input.txt") as f:
    return [x for x in f.read().split("\n\n") if x]

def part1():
  part1 = 0
  fields = ['byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:']
  for line in get_data():
    part1 += all(x in line for x in fields)
  return part1

print(f'Part 1: {part1()}')
