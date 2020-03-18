def ok (a) :
  return a < 13 or a > 19 or a == 15 or a == 16

def no_teen_sum(a, b, c):
  sum = 0
  if ok (a) :
    sum += a
  if ok (b)  :
    sum += b
  if ok (c) :
    sum += c
  return sum
