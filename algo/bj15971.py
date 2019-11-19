import sys

def DFS(strt, dest):
    global con
    global path
    global visited
    if strt == dest:
        return True
    else:
        for nxt in con[strt]:
            if visited[nxt] ==False:
                visited[nxt] =  True
                checker = DFS(nxt, dest)
                if checker == True:
                    path.append(nxt)
                    return True
    return False
con = dict()
path = []
N, R1, R2 = map(int, sys.stdin.readline().split())
val = dict()
for _ in range(N-1):
    r1,r2,tunnel = map(int,sys.stdin.readline().split())
    try:
        con[r1].append(r2)
    except:
        con[r1] = [r2]
    try:
        con[r2].append(r1)
    except:
        con[r2] = [r1]
    try:
        temp = val[r1]
        temp[r2] = tunnel
        val[r1] = temp
    except:
        val[r1] = {r2:tunnel}
    try:
        temp = val[r2]
        temp[r1] = tunnel
        val[r2] = temp
    except:
        val[r2] = {r1:tunnel}
if  R1==R2:
    print(0)
elif R2 in con[R1]:
    sys.stdout.write("0")
else:
    visited =dict()
    for i in con:
        visited[i] = False
    DFS(R1,R2)
    path.pop(0)
    cnt = 0
    while path:
        if val[R2][path[0]] > val[R1][path[-1]]:
            cnt += val[R1][path[-1]]
            R1 = path[-1]
            path.pop(-1)
        else:
            cnt += val[R2][path[0]]
            R2 = path[0]
            path.pop(0)
    print(cnt)

