n = int(input())
nums = list(map(int, input().split()))
cnt = 0
for i in range(n):
    if(nums[i] > 0):
        cnt += 1
print(cnt)
