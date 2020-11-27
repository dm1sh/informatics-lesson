for x in range(1, 1000):
  xx = x
  x0 = x
  n = 0
  while xx > 0:
    d = xx % 3
    n = 10*n + d
    xx //= 3
  if n // 100000 > 0:
    print(x)
    break

# 244
