def sum2(nums):
  sum = 0
  for i in range(min(2,len(nums))):
    sum += nums[i]
  return sum

