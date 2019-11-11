import sys
from math import factorial
n1, n2 = map(int, sys.stdin.readline().split())
print(int(factorial(n1)//(factorial(n2)*factorial(n1-n2)))%10007)
