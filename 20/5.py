for x in range(100, 10000):
  xx = x
  l = xx - 16
  m = xx + 16
  while l != m:
    if l > m:
      l -= m
    else:
      m -= l
  if m == 16:
    print(x)
    break

# 128
