# https://www.acmicpc.net/problem/10984
# O(n^2)

import sys

T = int(sys.stdin.readline().rstrip())
for i in range(T):
    N = int(sys.stdin.readline().rstrip())
    gpa = 0
    credit = 0
    for j in range(N):
        temp_credit, temp_gpa = map(float, sys.stdin.readline().split())
        #print('credit :',credit,'gpa :', gpa)
        gpa = (temp_credit*temp_gpa + gpa*credit)/(credit+temp_credit)
        credit += temp_credit

    print(int(credit), '%.1f'%gpa)

