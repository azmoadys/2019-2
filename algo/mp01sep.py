integer = [8, 7, 2, 5, 3, 1]
#S = 10

def solution(integer, S):
    for i in integer:
        temp = integer
        temp.remove(i)
        if S-i in temp:
            print('(',i,'+',S-i,'=',S,')')
            return True
    return False

if __name__ == '__main__':
    S = int(input())
    print(solution(integer, S))
