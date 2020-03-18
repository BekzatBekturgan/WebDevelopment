def sum13(nums):
      if len(nums)==0: return (0)
  sum = 0
  if nums[0] != 13: sum+=nums[0]
  for i in range(1, len(nums)):
    if nums[i] == 13:
      continue
    elif nums[i-1] == 13:
      continue
    else: sum+=nums[i]
  return sum
