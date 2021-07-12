
N = int(input())
arr =list(map(int, input().split()))

dp= [0] * (N)
for i in range(N):
    if dp[i-1]> 0:
        dp[i] = dp[i-1] + arr[i] 
    else:
        dp[i] = arr[i]
print(max(dp))