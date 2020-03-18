n = int(input())
nums = list(map(int, input().split()))
for i in range(n):
    if nums[i] % 2 == 0:
        print(nums[i], end=" ")
