k = 0
for x in range(-1000, 1000):
  xx = x
  a, b = 0, 1
  while xx > 0:
    a += 1
    b *= xx % 10
    xx //= 10
  if a == 2 and b == 0:
    k += 1
print(k)

# 9
