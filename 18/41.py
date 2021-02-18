def count(a: list[list[int]], i: int, j: int, prev: int, n: int):
  if j == n or i == n or j == -1 or i == -1 or a[i][j] <= prev:
    return 0
  else:
    summ = a[i][j]

    summ += max(count(a, i+1, j, a[i][j], n), count(a, i, j+1, a[i][j], n),
                count(a, i-1, j, a[i][j], n), count(a, i, j-1, a[i][j], n))
    return summ


with open('dat/18-k2.csv', 'r') as f:
  a = [[int(i) for i in row.split()] for row in f.readlines()]
  m = 0
  for i in range(len(a)):
    for j in range(len(a)):
      m = max(m, count(a, i, j, -1, len(a)))

print(m)

# 446
