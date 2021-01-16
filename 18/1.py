n = int(input())

with open('./input.txt', 'r') as f:
  arr = [f.readline().split() for i in range(n)]
  steps = (n - 1) * 2