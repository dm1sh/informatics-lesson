for d in range(1, 10000):
  dd = d
  n, s = 1, 46
  while s <= 2700:
    s += dd
    n += 4
  if n == 121:
    print(d)
    break

# 89
