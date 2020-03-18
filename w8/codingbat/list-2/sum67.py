def sum67(nums):
      sum = 0
  test = False
  for i in range(len(nums)):
    if nums[i] == 6 and test== False:
      test = True
    elif nums[i] == 7 and test:
      test = False
    elif test == False : sum+=nums[i]
  return sum
