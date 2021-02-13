def count(a, i, j):
  if i == -1 or j == -1:
    return None

  l = count(a, i, j-1)
  t = count(a, i-1, j)
  c = a[i][j] // 8

  if l == None and t == None:
    return [c, c]
  if l == None:
    return [c + t[0], c + t[1]]
  if t == None:
    return [c + l[0], c + l[1]]

  return [c + max(t[0], l[0]), c + min(t[1], l[1])]


a = [[int(i) for i in row.split(';')] for row in open('dat/18-2.csv', 'r')]

res = count(a, len(a)-1, len(a[0])-1)

print(res[0] * 8, res[1] * 8)

# 1256 472
