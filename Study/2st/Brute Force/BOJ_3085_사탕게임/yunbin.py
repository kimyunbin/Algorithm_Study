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
