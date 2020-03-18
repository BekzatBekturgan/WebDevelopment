def make_bricks(small, big, goal):
  k = goal // 5
  return min(k,big) * 5 + small >= goal
