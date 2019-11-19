import sys

def NXT(room,point,state): # point 현재 위치 / state 현재 움직임(1:왼쪽, 2:대각선, 3:아래쪽)
    if point == N*N: # 끝에 도착하면 cnt 증가
        global cnt
        cnt += 1
    else:
        row = int((point-1)//N)
        col = (point-1)%N
        if state == 1:
            if col+1<N and room[row][col+1]!=1:
                NXT(room, point+1,1)
            if col+1<N and row+1<N and room[row+1][col+1]!=1 and room[row][col+1]!=1 and room[row+1][col]!=1:
                NXT(room, point+N+1,2)
        elif state == 2:
            if col+1<N and room[row][col+1]!=1:
                NXT(room, point+1,1)
            if col+1<N and row+1<N and room[row+1][col+1]!=1 and room[row][col+1]!=1 and room[row+1][col]!=1:
                NXT(room, point+N+1,2)
            if row+1<N and room[row+1][col]!=1:
                NXT(room, point+N,3)
        else:
            if col+1<N and row+1<N and room[row+1][col+1]!=1 and room[row][col+1]!=1 and room[row+1][col]!=1:  
                NXT(room, point+N+1,2)
            if row+1<N and room[row+1][col]!=1:
                NXT(room, point+N,3)
        
cnt = 0
N = int(sys.stdin.readline())
room = []
for _ in range(N):
    room.append(list(map(int, sys.stdin.readline().split())))
first_state = 1
first_point = 2
NXT(room,first_point,first_state)
sys.stdout.write(str(cnt))
