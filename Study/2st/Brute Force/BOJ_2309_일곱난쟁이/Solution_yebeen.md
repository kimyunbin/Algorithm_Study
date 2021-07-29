```python
height = []
for i in range(9):
    height.append(int(input()))

two = sum(height) - 100
end = 0
for i in range(9):
    if end == 1:
        break
    for j in range(9):
        if height[j] == height[i]:
            continue
        if height[i] + height[j] == two:
            le = height[j]
            height.remove(height[i])
            height.remove(le)
            end = 1
            break
height.sort()
for i in range(7):
    print(height[i])
```

1. 아홉명의 키의합 -  100 = 난쟁이가 아닌 두명의 키의 합

2. 2중 for문을 돌며 그 두명의 키의 합의 조합을 찾는다.

​	2.1 두명의 합이 아홉명 합에서 100을 뺀거와 같다면 remove해서 height배열에서 빼준다.

​	2.2 하나 remove해주었을때 그 다음것도 remove해줘야하는데 앞에것을 제거했으므로 인덱스가 달라진다. 그래서 le라는 변수에 두번째로 제거할 값 height[j] 값을 저장한뒤 remove시켜줬다.

​    2.3 sort하고 출력