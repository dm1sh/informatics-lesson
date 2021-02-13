with open('dat/18-k1.csv', "r") as f:
  k = 0
  m = 0
  for i in f.readlines():
    if int(i) % 2 == 1:
      k += 1
    else:
      if k > m:
        m = k
      k = 0

  print(m)

# 5