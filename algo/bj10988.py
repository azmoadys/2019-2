# https://www.acmicpc.net/problem/10988

word = input()
length = len(word)
check = 1
for i in range(int(length/2)):
    if word[i] != word[length-i-1]:
        check = 0
print(check)
