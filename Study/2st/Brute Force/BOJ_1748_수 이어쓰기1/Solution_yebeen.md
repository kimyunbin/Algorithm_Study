# 1748.수 이어 쓰기 1 

| 시간 제한                                                    | 메모리 제한 | 제출  | 정답 | 맞은 사람 | 정답 비율 |
| :----------------------------------------------------------- | :---------- | :---- | :--- | :-------- | :-------- |
| 0.15 초 ([하단 참고](https://www.acmicpc.net/problem/1748#)) | 128 MB      | 12815 | 5835 | 4920      | 50.890%   |

## 문제

1부터 N까지의 수를 이어서 쓰면 다음과 같이 새로운 하나의 수를 얻을 수 있다.

> 1234567891011121314151617181920212223...

이렇게 만들어진 새로운 수는 몇 자리 수일까? 이 수의 자릿수를 구하는 프로그램을 작성하시오.

## 입력

첫째 줄에 N(1 ≤ N ≤ 100,000,000)이 주어진다.

## 출력

첫째 줄에 새로운 수의 자릿수를 출력한다.

## 예제 입력 1 

```
5
```

## 예제 출력 1 

```
5
```

## 예제 입력 2 

```
15
```

## 예제 출력 2 

```
21
```

## 예제 입력 3 

```
120
```

## 예제 출력 3 

```
252
```

## 코드

```python
N=int(input())
res = 0
s = len(str(N))
if s == 1:
    res = N
else:
    for i in range(2,s+1):
        res += (9*(10**(i-2))*(i-1))
    res += (N-(10**(s-1)-1))*s
print(res)
```

## 풀이

한 자리 수 일 때는 받아온 N그대로이니까 N출력

한자리수 이외에는 만약 3자리수이라면 한자리수 * 9개, 두 자리수* 90개를 모두 더해준뒤 

N-99(두자리수중 가장 큰것)을 하면 세자리수의 갯수가 나온다.

그래서 그 갯수에 *3을 한 것을 더해줘서 출력했다.