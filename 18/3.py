# 345

with open('./dat/18-17.txt', 'r') as f:
  p = float('+inf')
  s = 0
  ms = float('-inf')

  for sn in f.readlines():
    n = float(sn)
    if n < p:
      s += n
    else:
      if s > ms:
        ms = s
      s = 0
    p = n

print(int(ms))
