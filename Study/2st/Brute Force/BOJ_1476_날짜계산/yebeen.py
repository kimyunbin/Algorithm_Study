E1,S1,M1 = map(int,input().split())
cnt = 0
E,S,M =0,0,0
while(1):
    cnt += 1
    E += 1
    S += 1
    M += 1
    if E >= 16:
        E -= 15
    if S >= 29:
        S -= 28
    if M >= 20:
        M -= 19
    if E == E1 and  S== S1 and M == M1:
        break
print(cnt)