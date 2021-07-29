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