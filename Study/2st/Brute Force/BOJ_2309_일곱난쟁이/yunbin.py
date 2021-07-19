
arr = [int(input()) for _ in range(9)]
target = sum(arr) - 100
for i in range(len(arr)):
    temp = target - arr[i]
    if temp != arr[i] and temp in arr:
        arr.remove(temp)
        arr.pop(i)
        break

arr.sort()
print(*arr,sep='\n')
