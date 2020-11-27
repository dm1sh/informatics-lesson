for x in reversed(range(1, 10000)):
  xx = x
  q = 6
  l = 0
  while xx >= q:
    l += 1
    xx -= q
  m = xx
  if m < l:
    m = l
    l = xx
  if l == 3 and m == 5:
    print(x)
    break

# 33
