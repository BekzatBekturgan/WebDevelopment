def find_min(a, b, c, d):
    return min(a, min(b, min( c, d)))
nums = list(map(int, input().split()))
n1 = nums[0]
n2 = nums[1]
n3 = nums[2]
n4 = nums[3]
print(find_min(n1, n2, n3, n4))