f = open("input.txt", "r")
values = f.read().split()

passwords = values[2::3]
letters = [i[:-1] for i in values[1::3]]
mins_maxes = values[::3]
mins = [i[0:i.index("-")] for i in mins_maxes]
maxes = [i[i.index("-")+1:] for i in mins_maxes]

def pw_2_check(pw, letter, ind1, ind2):
  count = 0
  if pw[ind1-1] == letter:
    count += 1
  if pw[ind2-1] == letter:
    count += 1
  return count == 1

def pw_2_check_all(passwords, letters, inds1, inds2):
  count = 0
  for i in range(len(passwords)):
    pw = passwords[i]
    letter = letters[i]
    ind1 = int(inds1[i])
    ind2 = int(inds2[i])
    if pw_2_check(pw, letter, ind1, ind2):
      count += 1
  return count
print("Part 2: ", pw_2_check_all(passwords, letters, mins, maxes))
