n = int(input())
li = list(map(int, input().split()))
dp = [0]*n
for i in range(n):
    dp[i] = (dp[i-1] + li[i]) if dp[i-1] > 0 else li[i]
print(max(dp))