#https://programmers.co.kr/skill_checks/41973

arr1 = [1,1,3,3,0,1,1]
arr2 = [4,4,4,3,3]

def solution(arr):
    dic = dict()
    answer = []
    length = len(arr)
    answer.append(arr[0])
    cnt = 0
    for i in range(1, length):
        if arr[i] !=  answer[cnt]:
            cnt+=1
            answer.append(arr[i])
    return answer

if __name__ == '__main__':
    print(solution(arr1))
    print(solution(arr2))	
