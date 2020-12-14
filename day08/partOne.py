instructions = []
with open('input.txt') as fp:
  line = fp.readline()
  while line:
    tokens = line.strip().split()
    instructions.append((tokens[0], int(tokens[1])))
    line = fp.readline()

def execute(instrs):
  hasLoop = False
  visited = set()
  ptr = acc = 0
  while ptr < len(instrs):
    op, value = instrs[ptr]
    if ptr in visited:
      hasLoop = True
      break
    visited.add(ptr)
    if op == 'jmp':
      ptr = ptr + value
      continue
    elif op == 'acc':
      acc = acc + value
    ptr = ptr + 1
  return (acc, hasLoop)
  
  partOne = {execute(instructions)[0]}
  print(partOne)
