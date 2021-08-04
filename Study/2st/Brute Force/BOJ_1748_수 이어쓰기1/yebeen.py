N=int(input())
res = 0
s = len(str(N))
if s == 1:
    res = N
else:
    for i in range(2,s+1):
        res += (9*(10**(i-2))*(i-1))
    res += (N-(10**(s-1)-1))*s
print(res)