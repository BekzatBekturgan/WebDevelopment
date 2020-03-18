import math
n = int(input())
k = round(math.log2(n))
if n == 2 ** k:
    print("YES")
else: 
    print("NO")
