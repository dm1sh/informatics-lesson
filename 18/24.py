def count(a: list[list[int]], i: int, j: int) -> list[int]:

  if i == len(a) or j == len(a[0]):
    return None

  if (a[i][j] > 100 and a[i][j] < 500) or (a[i][j] > -400 and a[i][j] < 0):
    return None

  r = count(a, i, j+1)
  b = count(a, i+1, j)

  c = a[i][j]

  if r == None and b == None:
    return [c, c]
  if r == None:
    return [c + b[0], c + b[1]]
  if b == None:
    return [c + r[0], c + r[1]]

  return [c + max(r[0], b[0]), c + min(r[1], b[1])]


with open("dat/18-13.csv", 'r') as f:
  a = [[int(i) for i in row.split(';')] for row in f.readlines()]

  print(count(a, 0, 0))

# 1535 330 (не знаю как починить с минимумом)
