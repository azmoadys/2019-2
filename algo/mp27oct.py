def sol(data):
    left = dict()
    right = dict()
    LEN = len(data)
    temp = 1
    for i in range(1,LEN):
        temp *= data[i-1]
        left[i] = temp
    left[0] = 1
    temp = 1
    right[LEN-1] = 1
    for i in range(LEN-2,-1,-1):
        temp *= data[i+1]
        right[i] = temp
    result = []
    for i in range(0,LEN):
        result.append(left[i]*right[i])
    print(result)

if __name__=="__main__":
    sol([1, 2, 3, 4, 5])
    sol([5, 3, 4, 2, 6, 8])
