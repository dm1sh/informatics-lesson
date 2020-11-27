s, t = 5, 25
c = [15]
n = [12]
arr = [1] * (s + 1)

for k in range(len(c) + 1):
  s__ = s + 1 if k == 0 else c[k - 1] + 1
  s_ = s__ - 1
  t__ = c[k] + 1 if k < len(c) else t + 1
  t_ = t__ - 1
  for i in range(s__, t__):
    e = 0
    if i - 1 >= s_ and not i - 1 in n:
      e += arr[i - 1]
    if i - 3 >= s_ and not i - 3 in n:
      e += arr[i - 3]
    arr.append(e)
  back = arr[t_]
  arr = [0] * (t_ + 1)
  arr[t_] = back

print(arr[t])

# 280
