def close_far(a, b, c):
  ta = a
  tb = b
  tc = c
  a = min(ta,min(tb,tc) )
  c = max(ta,max(tc,tb) )
  b = ta + tb + tc - a - c
  return not(a + 1 == b and b + 1 == c)
  
