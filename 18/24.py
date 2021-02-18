def count(a: list[list[int]], i: int, j: int) -> list[int]:

  if i == len(a) or j == len(a[0]):
    return None

  if (a[i][j] > 100 and a[i][j] < 500) or (a[i][j] > -400 and a[i][j] < 0):
    return None

  r = count(a, i, j+1)
  b = count(a, i+1, j)

  c = a[i][j]

  if r == None and b == None and i == len(a)-1 and j == len(a[0])-1:
    return [[c, [[i, j]]], [c, [[i, j]]]]
  if r == None and b == None:
    return None
  if r == None:
    return [[c + b[0][0], [*b[0][1], [i, j]]], [c + b[1][0], [*b[1][1], [i, j]]]]
  if b == None:
    return [[c + r[0][0], [*r[0][1], [i, j]]], [c + r[1][0], [*r[1][1], [i, j]]]]

  mmax = max(r[0][0], b[0][0])
  mmin = min(r[1][0], b[1][0])

  Marr = r[0][1] if mmax == r[0][0] else b[0][1]
  marr = r[1][1] if mmin == r[1][0] else b[1][1]

  return [[c + mmax, [*Marr, [i, j]]], [c + mmin, [*marr, [i, j]]]]


with open("dat/18-13.csv", 'r') as f:
# with open("24.csv", 'r') as f:
  a = [[int(i.strip()) for i in row.split(';')] for row in f.readlines()]

  ret = count(a, 0, 0)

  print(ret[0])
  print(ret[1])

# 1535 975
