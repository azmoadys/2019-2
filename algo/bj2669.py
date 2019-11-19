import sys
cnt=0
mat = [[0]*100 for _ in range(100)]
for _ in range(4):
    x1,y1,x2,y2 = map(int, sys.stdin.readline().split())
    for  i in range(x1,x2):
        for j in range(y1,y2):
            mat[i][j] +=1
            if mat[i][j] == 1:
                cnt+=1
print(cnt)
