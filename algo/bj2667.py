import sys
sys.setrecursionlimit(1500)
def DFS(row,col,cnt):
    global MAP
    global visited
    global cnt_list
    if row < 0 or col < 0 or row>=N or col>=N:
        return 0
    elif MAP[row][col] == 0 or visited[row][col] ==True:
        return 0
    else:
        try:
            cnt_list[cnt]+=1
        except:
            cnt_list.append(1)
        MAP[row][col] = cnt
        visited[row][col] = True
        DFS(row-1,col,cnt)
        DFS(row+1,col,cnt)
        DFS(row,col-1,cnt)
        DFS(row,col+1,cnt)

N = int(sys.stdin.readline())
MAP=[]
visited = [[False]*N for _ in range(N)]
for _ in range(N):
    MAP.append(list(map(int,list(sys.stdin.readline().strip()))))

cnt = 1
cnt_list= [0]
#cnt_list = [0 for i in range(N*N)]
for i in range(N):
    for j in range(N):
        if MAP[i][j] != 0 and visited[i][j] ==False:
            DFS(i,j,cnt)
            cnt+=1
LEN = len(cnt_list)
cnt_list.sort()
print(LEN-1)
for i in range(1,LEN):
    print(cnt_list[i])
