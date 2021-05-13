def compute_lcm(x, y): 
  if(x > y):
    greater = x
  if(y > x):
    greater = y
  while(True):
    if(greater % x == 0 and greater % y == 0):
      return greater
    else:
      greater += 1
      continue


def compute_gcf(x, y): 
  if(x < y):
    smaller = x
  if(y < x):
    smaller = y
  for i in range(1, smaller + 1):
    if(x % i == 0 and y % i == 0):
      smaller = i
  return smaller 