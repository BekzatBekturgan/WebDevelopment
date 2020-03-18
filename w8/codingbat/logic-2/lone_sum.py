def lone_sum(a, b, c):
  sum = 0
  if a - b != 0 and a - c != 0 :
    sum += a
  if a - b != 0 and b - c != 0 : 
    sum += b
  if a - c != 0 and b - c != 0 :
    sum += c
  return sum 
