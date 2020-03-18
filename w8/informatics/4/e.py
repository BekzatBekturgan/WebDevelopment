n = int(input())
nums = list(map(int, input().split()))
for i in range(n - 1):
    if(nums[i] * nums[i + 1] > 0):
        print("YES")
        exit(0)
print("NO")