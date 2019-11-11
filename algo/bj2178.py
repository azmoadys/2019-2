import sys 
row, col = map(int, sys.stdin.readline().split()) 
data = [[0]*col for _ in range(row)] 
for i in range(row):
    temp = list(map(int,sys.stdin.readline().split()))
    print(temp)
    for j in range(col):
        print(temp[j])
        data[i][j] = temp[j]
print(data)




