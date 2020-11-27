m, M = 10000000, -1
for d in range(1, 10000000):
  dd = d
  n, s = 0, 24
  while s <= 1318:
    s += dd
    n += 15
  if n == 195:
    if d < m:
      m = d
    if d > M:
      M = d
print(m, M)

# 100 107
