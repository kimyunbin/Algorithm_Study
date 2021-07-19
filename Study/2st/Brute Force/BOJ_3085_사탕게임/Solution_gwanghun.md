# 사탕게임

> 브루트 포스

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

## 예제 입력 1 

```
3
CCP
CCP
PPC
```

## 예제 출력 1 

```
3
```

## 예제 입력 2 

```
4
PPPP
CYZY
CCPY
PPCC
```

## 예제 출력 2 

```
4
```

## 예제 입력 3 

```
5
YCPZY
CYZZP
CCPPP
YCYZC
CPPZZ
```

## 예제 출력 3 

```
4
```

## Code

```python
def checkBoard():
    global cnt, N
    for y in range(N):
        cnt_y, cnt_x = 1, 1
        for x in range(N):
            if x > 0:
                if board[y][x] == board[y][x-1]:
                    cnt_x += 1
                else:
                    cnt_x = 1

                if board[x][y] == board[x-1][y]:
                    cnt_y += 1
                else:
                    cnt_y = 1
            cnt = max(cnt, cnt_x, cnt_y)

N = int(input())
board = [list(input()) for _ in range(N)]
cnt = 0

for y in range(N):
    for x in range(N):
        if y < N-1 and board[y+1][x] != board[y][x]:
            board[y+1][x],board[y][x] = board[y][x],board[y+1][x]
            checkBoard()
            board[y+1][x],board[y][x] = board[y][x],board[y+1][x]
        if x < N-1 and board[y][x+1] != board[y][x]:
            board[y][x+1],board[y][x] = board[y][x],board[y][x+1]
            checkBoard()
            board[y][x+1],board[y][x] = board[y][x],board[y][x+1]

print(cnt)
```

## Review

- 보드의 인접한요소를 바꿀때, 자신의 오른쪽과 아래쪽 보드만 교환하면, 모든 인접한 요소를 한번씩 바꾸게 된다. 
- 바뀐 보드를 `checkBoard`로 검사한다. 
