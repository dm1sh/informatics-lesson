inf = float('inf')


def count(a: list[list[int]], i: int, j: int) -> list[int]:
  if a[i][j] > 100 and a[i][j] < 500 or a[i][j] < 0 and a[i][j] > -400:
    return [0, inf]

  t, l = [0, inf], [0, inf]
  summ = a[i][j]

  if i > 0:
    t = count(a, i-1, j)
  if j > 0:
    l = count(a, i, j-1)

  # minn = min(t[1], l[1])

  return [summ + max(t[0], l[0]), summ + min(t[1], l[1])]


with open("dat/18-13.csv", 'r') as f:
  a = [[int(i) for i in row.split(';')] for row in f.readlines()]

  print(count(a, len(a) - 1, len(a[0]) - 1))

# 1535
