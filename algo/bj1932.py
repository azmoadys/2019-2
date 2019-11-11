import sys
num = int(sys.stdin.readline().strip())
value = [[0]*num for i in range(num)]
result = [[0]*num for i in range(num)]
for i in range(num):
    value[i] = sys.stdin.readline().split()
    for j in range(i+1):
        value[i][j] = int(value[i][j])

for i in range(num):
    for j in range(i+1):
        if i==0:
            result[i][j] = value[i][j]
        else:
            if j>i-1:
                result[i][j] = value[i][j] + result[i-1][j-1]
            elif j-1<0:
                result[i][j] = value[i][j] + result[i-1][j]
            else:
                result[i][j] = value[i][j] + max(result[i-1][j-1],result[i-1][j])

max_val = 0
for i in result[num-1]:
    if i > max_val:
        max_val = i
print(max_val)
