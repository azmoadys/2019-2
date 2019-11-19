import sys

N = int(sys.stdin.readline())
for _ in range(N):
    A = {1:0,2:0,3:0,4:0}
    B = {1:0,2:0,3:0,4:0}
    temp_a = list(map(int,sys.stdin.readline().split()))
    temp_b = list(map(int,sys.stdin.readline().split()))
    for i in temp_a[1:]:
        A[i] +=1
    for i in temp_b[1:]:
        B[i] +=1
    Draw = True
    for i in range(4,0,-1):
        if A[i]>B[i]:
            print("A")
            Draw = False
            break
        elif A[i]<B[i]:
            print("B")
            Draw = False
            break
    if Draw:
        print("D")
