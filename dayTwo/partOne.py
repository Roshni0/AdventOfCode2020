f = open("input.txt", "r")
values = f.read().split()

passwords = values[2::3]
letters = [i[:-1] for i in values[1::3]]
mins_maxes = values[::3]
mins = [i[0:i.index("-")] for i in mins_maxes]
maxes = [i[i.index("-")+1:] for i in mins_maxes]

def pw_check(pw, letter, min, max):
  count = 0
  for char in pw:
    if char == letter:
      count += 1
      if count > max:
        return False
  return count >= min

def pw_check_all(passwords, letters, mins, maxes):
  count = 0
  for i in range(len(passwords)):
    pw = passwords[i]
    letter = letters[i]
    min = int(mins[i])
    max = int(maxes[i])
    if pw_check(pw, letter, min, max):
      count += 1
  return count
print("Part 1: ", pw_check_all(passwords, letters, mins, maxes))
