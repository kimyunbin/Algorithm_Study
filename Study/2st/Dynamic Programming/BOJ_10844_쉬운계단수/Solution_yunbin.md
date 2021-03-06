## 문제

45656이란 수를 보자.

이 수는 인접한 모든 자리수의 차이가 1이 난다. 이런 수를 계단 수라고 한다.

세준이는 수의 길이가 N인 계단 수가 몇 개 있는지 궁금해졌다.

N이 주어질 때, 길이가 N인 계단 수가 총 몇 개 있는지 구하는 프로그램을 작성하시오. (0으로 시작하는 수는 없다.)

## 입력

첫째 줄에 N이 주어진다. N은 1보다 크거나 같고, 100보다 작거나 같은 자연수이다.

## 출력

첫째 줄에 정답을 1,000,000,000으로 나눈 나머지를 출력한다.

## 예제 입력 1 복사

```
1
```

## 예제 출력 1 복사

```
9
```

## 예제 입력 2 복사

```
2
```

## 예제 출력 2 복사

```
17
```



## 풀면서 느낀점

으하... 공식 찾느라 애먹은 문제였다

자리수를 끝자리 기준으로 점화식을 세워야되는데 앞자리 기준으로 세우니까 반복패턴이 눈에 보이지 않았다. (0으로 시작하는 수는 없다) 이거때문에 시작수가 1 2 3 4 ...인줄 ? 

일단 3자리수까지는 숫자적어보면서 점화식을 찾아보자!

풀이방법은 일단은 가장뒤에 나올 숫자를 고정되었다고 생각해보자 예를 들자면? 2로 생각하자 

10의자리수는 1과 3밖에 올수없다. 그러므로 보편적인 패턴은 그전 자리수의 양옆의 경우의 수를 더해서 만들어지는것이다.

식으로 표현하자면 dp\[3][2] = dp\[2][1]+ dp\[2][3] 으로 가져올 수 있다. 

0의자리수와 9의 자리수는 양옆이 없기에 예외처리를 해주면 된다. 



| 자리수 | 0    | 1     | 2     | 3     | 4    | 5    | 6    | 7    | 8    | 9    |
| ------ | ---- | ----- | ----- | ----- | ---- | ---- | ---- | ---- | ---- | ---- |
| 1      | 0    | 1     | 1     | 1     | 1    | 1    | 1    | 1    | 1    | 1    |
| 2      | 1    | **1** | 2     | **2** | 2    | 2    | 2    | 2    | 2    | 1    |
| 3      | 1    | 3     | **3** | 4     | 4    | 4    | 4    | 4    | 3    | 2    |



## 나의 코드

```python
N = int(input())
dp = [[0] * 10 for _ in range(101)]

for j in range(1, 10):
    dp[0][j] = 1

for i in range(1, N+1):
    for j in range(10):

        if j == 0:
            dp[i][j] = dp[i - 1][1]
        elif j == 9:
            dp[i][j] = dp[i - 1][8]
        else:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]
print(sum(dp[N-1])%1000000000)
```