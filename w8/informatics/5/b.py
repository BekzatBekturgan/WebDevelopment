def calculate(a, n):
    return a ** n
nums = list(map(float, input().split()))
print(calculate(nums[0], nums[1]))