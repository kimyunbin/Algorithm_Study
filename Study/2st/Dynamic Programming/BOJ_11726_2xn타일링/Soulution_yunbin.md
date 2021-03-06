## 문제

2×n 크기의 직사각형을 1×2, 2×1 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.

아래 그림은 2×5 크기의 직사각형을 채운 한 가지 방법의 예이다.

![img](https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/11726/1.png)

## 입력

첫째 줄에 n이 주어진다. (1 ≤ n ≤ 1,000)

## 출력

첫째 줄에 2×n 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지를 출력한다.

## 예제 입력 1 복사

```
2
```

## 예제 출력 1 복사

```
2
```

## 예제 입력 2 복사

```
9
```

## 예제 출력 2 복사

```
55
```



## 풀면서 느낀점

DP의 점화식을 찾는 문제!! f(1) 부터 f(5)까지 그려보다보면 규칙을 찾을 수 있다 . 

![](https://images.velog.io/images/kimyunbin/post/ed2cd5d0-f8cd-427a-af6f-c73e3c2c9e73/IMG_DEED8EF3E48F-1.jpeg)

N= 4 일때를 예를 들어보자!  

총 다섯가지가 나오는데 두가지 경우로 나뉜다. 

N=3일때의 타일 + 세로 1개를 더하는 경우

N=2일때의 타일 + 2x2의 경우는 2가지의 경우가 나옴 



N= 5일때도 같은 방법으로 경우의 수를 구할 수 있고 점화식을 세울 수 있다 .

F(n) = F(n-1) + F(n-2)



## 나의 코드
```python
N = int(input())
if N == 1:
    print(1)
else:
    dp = [0 for _ in range(N + 1)]
    dp[1], dp[2] = 1, 2

    for i in range(3, N + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    print(dp[-1] % 10007)
```