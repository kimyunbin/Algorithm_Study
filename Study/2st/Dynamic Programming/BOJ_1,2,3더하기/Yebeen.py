T = int(input())
for tc in range(T):
    N = int(input())
    dp = [0]*(N+1)
    dp[1] = 1
    if N >1:
        dp[2] = 2
        if N > 2:
            dp[3] = 4

    if N >= 4:
        for i in range(4,N+1):
            dp[i] = dp[i-1]+dp[i-2]+dp[i-3]
    print(dp[N])