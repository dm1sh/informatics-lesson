# 1222

def add_10(matrix, x, y, dir):
  if (dir):
    if (x > 0 and x < len(matrix) - 1):
      return 10 if (matrix[x-1][y] % 2 == 0 and matrix[x+1][y] % 2 == 0) or (matrix[x-1][y] % 2 == 1 and matrix[x+1][y] % 2 == 1) else 0
  else:
    if (y > 0 and y < len(matrix[x]) - 1):
      return 10 if (matrix[x][y-1] % 2 == 0 and matrix[x][y+1] % 2 == 0) or (matrix[x][y-1] % 2 == 1 and matrix[x][y+1] % 2 == 1) else 0
  return 0


with open('./dat/18-J5.csv', 'r', encoding='utf-8-sig') as f:
  matrix = [[len(i.strip()) and int(i) for i in l.split(';')]
            for l in f.readlines()]
  arr = []

  for row_index, row in enumerate(matrix):
    new_row = []
    for el_index, el in enumerate(row):
      if row_index == 0 and el_index == 0:
        new_row.append(el)
      elif row_index == 0:
        new_row.append(new_row[el_index-1] + el)
      elif el_index == 0:
        new_row.append(arr[row_index-1][el_index] + el)
      else:
        ns = min(arr[row_index-1][el_index] + add_10(matrix, row_index, el_index, 0),
                 new_row[el_index-1] + add_10(matrix, row_index, el_index, 1)) + el
        new_row.append(ns)
    arr.append(new_row)

print(arr[-1][-1])
