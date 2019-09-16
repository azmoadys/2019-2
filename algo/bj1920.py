#https://www.acmicpc.net/problem/1920
#O(logn)

import sys

def search(A,N, length):
    low = 0
    high = length -1
    while low<=high :
        mid = (low+high)//2 
        if A[mid] > N:
            high = mid -1
        elif A[mid] < N:
            low = mid + 1
        else:
            return True
    return False

if __name__=='__main__':
    N = int(sys.stdin.readline().rstrip())
    A = input().split()
    for i in range(N):
        A[i] = int(A[i])
    M = int(sys.stdin.readline().rstrip())
    B = input().split()
    for i in range(M):
        B[i] = int(B[i])

    A.sort()

    for i in B:
        if search(A,i,N):
            print(1)
        else:
            print(0)

