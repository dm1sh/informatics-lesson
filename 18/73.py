def count(a, i, j):
  if i == len(a)-1:
    return [a[i][j], a[i][j]]

  M, m = count(a, i+1, j)

  res1, res2 = [M, m], [M, m]

  if j > 0:
    res1 = count(a, i+1, j-1)

  if j < len(a[0])-1:
    res2 = count(a, i+1, j+1)

  return a[i][j] + max(M, res1[0], res2[0]), a[i][j] + min(m, res1[1], res2[1])


a = [[int(i) for i in row.split(';')] for row in open('dat/18-0.csv', 'r')]

M, m = 0, float('inf')

for i in range(len(a[0])):
  res = count(a, 0, i)
  M = max(M, res[0])
  m = min(m, res[1])

print(M, m)

# 811 201
