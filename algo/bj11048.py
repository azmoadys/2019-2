import sys

row, col = map(int,sys.stdin.readline().split())
num = [[0]*col for i in range(row)]
for i in range(row):
    num[i] = sys.stdin.readline().split()
    for j in range(col):
        num[i][j] = int(num[i][j])

result = [[0]*col for i in range(row)]
result[0][0] = num[0][0]
for i in range(1,col):
    result[0][i] = result[0][i-1] + num[0][i]
for i in range(1,row):
    result[i][0] = result[i-1][0] + num[i][0]
for i in range(1,row):
    for j in range(1,col):
        result[i][j] = num[i][j]+max(result[i-1][j], result[i][j-1])
print(result[row-1][col-1])
