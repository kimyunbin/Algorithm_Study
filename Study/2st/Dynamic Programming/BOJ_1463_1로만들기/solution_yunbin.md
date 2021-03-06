## 문제

정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.

1. X가 3으로 나누어 떨어지면, 3으로 나눈다.
2. X가 2로 나누어 떨어지면, 2로 나눈다.
3. 1을 뺀다.

정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.

## 입력

첫째 줄에 1보다 크거나 같고, 106보다 작거나 같은 정수 N이 주어진다.

## 출력

첫째 줄에 연산을 하는 횟수의 최솟값을 출력한다.

## 예제 입력 1 복사

```
2
```

## 예제 출력 1 복사

```
1
```

## 예제 입력 2 복사

```
10
```

## 예제 출력 2 복사

```
3
```



## 풀면서 느낀점

그냥 무지성으로 1~3번까지 일단 코딩을 해보고 나니까 10 9 3 1은 그리디로 풀 수 있지 않았다. 거기에 if 문으로 어떻게 해도 답은 나오지 않았다. 

이것이 DP의 시작이였다...

<br>

푸는법은 DP 배열은 정수 i에서 가장 작은 연산으로 만들 수 있는 최솟값을 저장한다.

인덱스는 숫자, 저장값은 연산 사용 횟수의 최소값을 저장한다. 



최솟값을 만든다는 것은 예를 들자면 X가 9일때 3으로 나누어떨어지기 때문에 

역으로 3에서 연산 x3 을 한번만 한다면 9가 나온다는걸 식으로 표현하자면 

dp[9//3] 에서 연산횟수+1 이라고 볼 수 있다. 

풀이는 먼저 `1을 뺀다`를 먼저 실행한  dp.append(dp[i - 1] + 1) 

두번째로 3으로 나누어떨어지는지 체크

세번쨰로 2로 나누어떨어지는지 체크 

if~elif 문으로 하지 않은 이유는 6과 같이 중복되어있을 수 있기 때문에 가장 작은 최솟값을 찾기 위해 따로 if 문을 써줬다.

## 나의 코드

```python
N = int(input())

dp = [0, 0, 1, 1]

for i in range(4, N + 1):
    dp.append(dp[i - 1] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)

print(dp[N])

```

