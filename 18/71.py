def count(a, i, j):
  if i == -1 or j == -1:
    return None

  if a[i][j] > 100 and a[i][j] < 500:
    return None

  l = count(a, i, j-1)
  t = count(a, i-1, j)

  c = a[i][j] if a[i][j] % 3 == 0 or a[i][j] % 4 == 0 else 0

  if l == None and t == None and i == 0 and j == 0:
    return [c, c]
  if l == None and t == None:
    return None
  if l == None:
    return [c + t[0], c + t[1]]
  if t == None:
    return [c + l[0], c + l[1]]

  return [c + max(t[0], l[0]), c + min(t[1], l[1])]


a = [[int(i) for i in row.split(';')] for row in open('dat/18-11.csv', 'r')]

print(count(a, len(a)-1, len(a[0])-1))

# 1021 222
