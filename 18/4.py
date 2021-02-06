# 29

with open('./dat/18-77.txt', 'r') as f:
  p = float(f.readline())
  ms = float('-inf')
  s = 0

  for sn in f.readlines():
    n = float(sn)
    if abs(n - p) >= 20:
      s += n
      if s > ms:
        ms = s
    else:
      s = 0
    p = n

print(int(ms))
