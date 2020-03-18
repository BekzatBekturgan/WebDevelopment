n = int(input())
nums = list(map(int, input().split()))
cnt = 0
for i in range(0, n - 1):
    if(nums[i + 1] > nums[i]):
        cnt += 1
print(cnt)
