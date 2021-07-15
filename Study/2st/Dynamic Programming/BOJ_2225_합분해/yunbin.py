N, K = map(int,input().split())

dp = [[0] *201 for _ in range(201)]

for i in range(201):
    dp[i][1] = 1
#[][] : [n의자리수][k의 갯수]
for i in range(1,201):  # k의 갯수
    for j in range(201):
        for z in range(j+1):
            dp[j][i] += dp[z][i-1]
            dp[j][i] %= 1000000000
print(dp[N][K])
