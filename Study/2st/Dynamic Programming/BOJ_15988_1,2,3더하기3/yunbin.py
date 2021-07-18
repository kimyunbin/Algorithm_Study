TC = int(input())

arr = [int(input()) for _ in range(TC)]
N = max(arr)
dp = [0] * (N+1)
dp[1], dp[2], dp[3] = 1, 2, 4
for i in range(4, N+1):
    dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) %1000000009

for i in arr:
    print(dp[i])