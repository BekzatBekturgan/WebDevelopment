def round10(a):
  if a % 10 < 5 :
    return a - a % 10
  return a + 10 - a % 10

def round_sum(a, b, c):
  return round10(a) + round10(b) + round10(c)
