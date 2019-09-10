# https://mailprogramming.com/solution/54

data = [5, 6, -5, 5, 3, 5, 3, -2, 0]
S = 8

def solution(data,S):
    length = len(data)
    for i in range(0,length):
        check = sum(data[i:length])
        for j in range(length, i, -1):
            if check == S:
                answer = data[i:j]
                break
            check -= data[j-1]
        if check ==S:
            break
    return answer

if __name__ == "__main__":
    print(solution(data,S))
