integer = [8, 7, 2, 5, 3, 1]
#S = 10

def solution(integer, S):
    integer.sort()
    low = 0
    high = len(integer)-1
    if integer[high-1] +integer[high] < S:
        return False
    while low < high :
        if integer[low] +integer[high] == S:
            print(integer[low], integer[high])
            return True
        elif integer[low] +integer[high] > S:
            high -=1
        else:
            low+=1
    return False



if __name__ == '__main__':
    S = int(input())
    print(solution(integer, S))
