# link
# O(n^3)

data = [2, 0 , 2, 1, 4, 3, 1, 0]

def solution(data):
    answer = []
    length = len(data)
    cnt = 0
    for i in range(length):
        for j in range(length, i, -1):
            temp = data[i:j]
            #print(temp, '/', sum(temp), '/', (max(temp)-min(temp)+1)*(max(temp)+min(temp))/2)
            if sum(temp) == (max(temp)-min(temp)+1)*(max(temp)+min(temp))/2 and cnt<j-i-1:
                #print('in')
                cnt = j-i
                answer = temp
    return answer

if __name__ == "__main__":
    print(solution(data))
