# https://programmers.co.kr/skill_checks/41973?challenge_id=949

n1 = 121
n2 = 3

def solution(n):
    answer = 0
    while True:
        A = answer * answer
        if A !=n and A < n:
            answer += 1
        elif A == n:
            return (answer+1)*(answer+1)
        else :
            return -1
    return answer

if __name__ == '__main__':
    print(solution(n1))
    print(solution(n2))
