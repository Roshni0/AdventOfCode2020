def get_seat_id(s):
  return int(s.replace('F','0').replace('B','1')
              .replace('L','0').replace('R','1'), 2)

seat_ids = sorted(get_seat_id(s) for s in open('input.txt').readlines())
print('Max:', seat_ids[-1])
