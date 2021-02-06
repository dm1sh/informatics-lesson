with open('./dat/18-6.txt', 'r') as f:
  matrix = [[int(i) for i in e.split()] for e in f.readlines()]
  arr = []

  for row_index, row in enumerate(matrix):
    new_row = []
    for el_index, el in enumerate(row):
      if row_index == 0 and el_index == 0:
        new_row.append([matrix[0][0]] * 2)
      elif row_index == 0:
        new_row.append([new_row[el_index-1][0] + el] * 2)
      elif el_index == 0:
        new_row.append([arr[row_index-1][el_index][0] + el] * 2)
      else:
        ns = [max([arr[row_index-1][el_index][0], new_row[el_index-1][0]]) + el,
              min([arr[row_index-1][el_index][1], new_row[el_index-1][1]]) + el]
        new_row.append(ns)
    arr.append(new_row)

# for row in matrix:
#   for el in row:
#     print(el, end=' ')
#   print()

# print("-------------------------Delimeter-------------------------")

# for row in arr:
#   for el in row:
#     print(el, end=' ')
#   print()

print(arr[-1][-1])
