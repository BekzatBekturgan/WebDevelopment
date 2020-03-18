v = int(input())
t = int(input())
res = 0
if v > 0:
    res = (v * t) % 109
else:
    res = (109 - ( abs(v * t) % 109) )% 109
print(res)  