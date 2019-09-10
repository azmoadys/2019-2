# link

data1  = [3, 4, -7, 3, 1, 3, 1, -4, -2, -2]
data2 = [1,2,3,4,5,6,7,8,9]

def solution(data):
    dic = dict()
    dic[0] =0
    length = len(data)
    for i in range(length):
        temp =dic[i] +data[i]
        if temp in dic:
           return True
        dic[i+1] = temp
    return False
        
def printf(result):
    if result == True:
        return '부분 배열 존재'
    else:
        return '부분 배열 존재 하지 않음'


if __name__ == '__main__':
    print(data1,'\t', printf(solution(data1)))
    print(data2,'\t', printf(solution(data2)))
