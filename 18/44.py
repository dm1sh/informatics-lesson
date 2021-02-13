a = [int(i) for i in open('dat/18-k3.csv', 'r')]

k = 0
for i in range(len(a) - 5):
  for j in range(1, 6):
    if a[i] + a[j] < 100:
      k += 1

print(k)

# 15
