for x in range(1, 1000):
  a, b = 0, 1
  xx = x
  while xx > 0:
    if xx % 2 > 0:
      a += 1
    else:
      b += xx % 5
    xx //= 5
  if a == 2 and b == 9:
    print(x)
    break

# 605
