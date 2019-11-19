import sys
height = []
for i in range(9):
    height.append(int(sys.stdin.readline()))
total = sum(height)
result = height[:]
find = False
for i in range(9):
    for j in range(9):
        if i == j:
            continue
        if total-height[i] - height[j] == 100:
            find = True
            result.remove(height[i])
            result.remove(height[j])
            break
    if find == True:
        break
result.sort()
for num in result:
    print(num)
