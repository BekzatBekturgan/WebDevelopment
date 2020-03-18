def centered_average(nums):
      maxi = 0
  mini = 1e9
  sum = 0
  for i in range(len(nums)):
    sum+=nums[i]
    if nums[i] > maxi:
      maxi = nums[i]
    if nums[i] < mini:
      mini = nums[i]
  sum-=maxi
  sum-=mini
  return int(sum/(len(nums)-2))
