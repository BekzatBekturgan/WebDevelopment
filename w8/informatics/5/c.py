def xor(a, b):
    if(a == 1 and b == 1): return 0
    if(a == 0 and b == 0): return 0
    return 1
nums = list(map(int, input().split()))
n1 = nums[0]
n2 = nums[1]
print(xor(n1 , n2))