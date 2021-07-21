## 문제

상근이는 어렸을 적에 "봄보니 (Bomboni)" 게임을 즐겨했다.

가장 처음에 N×N크기에 사탕을 채워 놓는다. 사탕의 색은 모두 같지 않을 수도 있다. 상근이는 사탕의 색이 다른 인접한 두 칸을 고른다. 그 다음 고른 칸에 들어있는 사탕을 서로 교환한다. 이제, 모두 같은 색으로 이루어져 있는 가장 긴 연속 부분(행 또는 열)을 고른 다음 그 사탕을 모두 먹는다.

사탕이 채워진 상태가 주어졌을 때, 상근이가 먹을 수 있는 사탕의 최대 개수를 구하는 프로그램을 작성하시오.

## 입력

첫째 줄에 보드의 크기 N이 주어진다. (3 ≤ N ≤ 50)

다음 N개 줄에는 보드에 채워져 있는 사탕의 색상이 주어진다. 빨간색은 C, 파란색은 P, 초록색은 Z, 노란색은 Y로 주어진다.

사탕의 색이 다른 인접한 두 칸이 존재하는 입력만 주어진다.

## 출력

첫째 줄에 상근이가 먹을 수 있는 사탕의 최대 개수를 출력한다.

## 예제 입력 1 복사

```
3
CCP
CCP
PPC
```

## 예제 출력 1 복사

```
3
```

## 예제 입력 2 복사

```
4
PPPP
CYZY
CCPY
PPCC
```

## 예제 출력 2 복사

```
4
```

## 예제 입력 3 복사

```
5
YCPZY
CYZZP
CCPPP
YCYZC
CPPZZ
```

## 예제 출력 3 복사

```
4
```



## 풀면서 느낀점

dfs로 풀어야되나.... 사방향 탐색을 다해야하나 어렵게 생각하다가 n= 50밖에 안되기때문에 브루트포스로 풀어보자고 생각했다

하나하나 바꿔가면서 arr 자체를 가로와 세로의 수를 for문을 돌면서 체크하는 비효율적인방법...? 이긴하다

check 할때 result 문을 for 문안에 넣어야되는데 한칸 밖으로 꺼냈다가 틀렸다고 해서 여러가지 찾다가 .... 정신차리고 코드를 보고나니 잘못썻다 ㅋㅋ



## 나의 코드 

```python
N = int(input())

arr = [list(map(str, input())) for _ in range(N)]


def check_width():
    global result
    for i in range(N):
        count = 1
        for j in range(N - 1):
            if arr[i][j] == arr[i][j + 1]:
                count += 1
            else:
                count = 1
            result = max(result, count)


def check_height():
    global result
    for i in range(N):
        count = 1
        for j in range(N - 1):
            if arr[j][i] == arr[j + 1][i]:
                count += 1
            else:
                count = 1
            result = max(result, count)


result = 0
for i in range(N):
    for j in range(N - 1):
        arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j]

        check_width()
        check_height()

        arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j]

        arr[j][i], arr[j + 1][i] = arr[j + 1][i], arr[j][i]

        check_width()
        check_height()

        arr[j][i], arr[j + 1][i] = arr[j + 1][i], arr[j][i]

print(result)
```