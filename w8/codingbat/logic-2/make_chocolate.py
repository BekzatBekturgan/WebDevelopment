def make_chocolate(small, big, goal):
  k = goal // 5
  if min(k,big) * 5 + small < goal  :
    return -1
  return  goal - 5 *min(k,big)
