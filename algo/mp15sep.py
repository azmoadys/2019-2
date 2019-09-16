# Option. this problem should be O(n)

data = [1, 0, 1, 0, 1, 0, 0, 1]

import sys

def solution(data):
    answer = []
    for i in data:
        if i == 0:
            answer = [0]+answer #앞쪽에 붙이기
        else:
            answer = answer+[1]
    
    return answer

if __name__ == '__main__':
    print(solution(data))
