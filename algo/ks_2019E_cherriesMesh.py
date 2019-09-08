# problem URL
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050edb/0000000000170721

# algorithm == path finding

def selection():
    # black == 1 sugar,red == 2 sugar
    n,m = map(int, sys.stdin.readline().split()) # n = # of cherries / m = # of black strand
    #b_c = sys.stdin.readline().split()
    b_c = []
    while True:
        try:
            c,d = map(int,sys.stdin.readline().split())
            b_c.append([c,d])
        except:
            break
    #for i in range(len(b_c)):
    #    b_c[i] = int(b_c[i])

    for i in range(1,n+1):
        for j in range(i+1, n+1):
            if [i,j]        
 
    print(b_c)
    return result

import sys

test_case = int(input())

for i in range(test_case):
     print('Case #',i,': ',selection())
