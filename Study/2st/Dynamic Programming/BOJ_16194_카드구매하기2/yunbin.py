N = int(input())
arr = list(map(int,input().split()))
arr.insert(0,0)
dp = [9999999999]* (N+1)
dp[0] = 0
for i in range(1,N+1):
    for j in range(1,i+1):
        dp[i] = min(dp[i],dp[i-j] + arr[j])
print(dp[N])