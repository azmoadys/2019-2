import sys
from math import factorial
test_case = int(sys.stdin.readline())
for _ in range(test_case):
    n1, n2 = map(int, sys.stdin.readline().split())
    print(int(factorial(n2)/(factorial(n1)*factorial(n2-n1))))
