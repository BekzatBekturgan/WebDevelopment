N = int(input())
x = input()
a1 = x.split()
A = list(map(int, a1))
m = max(A)
for i in range(0, N):
    if max(A) == m:
        A.remove(max(A))
print(max(A))