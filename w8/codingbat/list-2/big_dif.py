def big_diff(nums):
    maxi = 0
    mini = 1e9
  for i in range(len(nums)):
    if nums[i] > maxi:
      maxi = nums[i]
    if nums[i] < mini:
      mini = nums[i]
  n = maxi - mini
  return n