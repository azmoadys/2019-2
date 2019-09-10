# link

data = [0, 0, 1, 0, 1, 0, 0]

def solution(data):
    cnt_0 = 0
    cnt_1 = 0
    result = []
    for i in data:
        if i == 0:
            cnt_0 +=1
        else:
            cnt_1 += 1
    cnt = min(cnt_0, cnt_1)
    length = len(data)
    for i in range(0, length-(2*cnt),1):
        temp = data[i:i+2*cnt]
        if temp.count(0) == cnt:
            result = temp
    return result

if __name__ =="__main__":
    print(solution(data))
