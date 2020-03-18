n = int(input())
nums = list(map(int, input().split()))
for i in range(n // 2):
    v = nums[n - i - 1]
    nums[n - i - 1] = nums[i]
    nums[i] = v
for i in range(n):
    print(nums[i], end=" ")