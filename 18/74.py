def count(a, i, j):
  if j == len(a[0])-1:
    return [a[i][j], a[i][j]]

  M, m = count(a, i, j+1)

  res1, res2 = [M, m], [M, m]

  if i > 0:
    res1 = count(a, i-1, j+1)

  if i < len(a)-1:
    res2 = count(a, i+1, j+1)

  return a[i][j] + max(M, res1[0], res2[0]), a[i][j] + min(m, res1[1], res2[1])


a = [[int(i) for i in row.split(';')] for row in open('dat/18-0.csv', 'r')]

M, m = 0, float('inf')

for i in range(len(a)):
  res = count(a, i, 0)
  M = max(M, res[0])
  m = min(m, res[1])

print(M, m)

# 785 176
