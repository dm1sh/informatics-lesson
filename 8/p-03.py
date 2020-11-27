for d in reversed(range(1, 1000000)):
  dd = d
  n, s = 0, 0
  while s <= 365:
    s += dd
    n += 5
  if n == 55:
    print(d)
    break

# 36
