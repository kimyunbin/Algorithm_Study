# 가장 긴 증가하는 부분 수열 4

> 다이내믹프로그래밍

## 문제

수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.

예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {**10**, **20**, 10, **30**, 20, **50**} 이고, 길이는 4이다.

## 입력

첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다.

둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000)

## 출력

첫째 줄에 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력한다.

둘째 줄에는 가장 긴 증가하는 부분 수열을 출력한다. 그러한 수열이 여러가지인 경우 아무거나 출력한다.

## 예제 입력 1

```
6
10 20 10 30 20 50
```

## 예제 출력 1 

```
4
10 20 30 50
```

## Code

```python
n = int(input())
li = list(map(int, input().split()))
dp = [1 for _ in range(n)]
for i in range(1, n):
    for j in range(i):
        if li[i] > li[j]:
            dp[i] = max(dp[i], dp[j]+1)
my_max = max(dp)
print(my_max)
r= []

idx = N
while my_max:
    for i in range(idx-1, -1, -1):
        if dp[i]==my_max:
            if (r and r[-1] > A[i]) or not r:
                r.append(A[i])
                idx = i
                my_max -= 1
                break

print(*r[::-1])
```

## Review

- `dp[i]`는 리스트의 i번째 까지 자신을 포함하는 가장 긴 수열의 길이이다.
- 2중 for문을 통해서 이전에 구해 놓은 값들과 비교를 해 현재 상태가 더 클 때, `dp[i]`에 추가시킬 수 있다. 
- `print(max(dp))`

- 위 과정은 이전 문제인 [가장긴 증하가는 부분수열](https://www.acmicpc.net/problem/11053)과 비슷하다. 
- dp[i]를 n이라고 생각해 보자 그렇다면 그다음의 값은 n+1인 dp[i+m]인 어떤 값이 들어와야 한다. 

