Input1 =  [1, 2, 3, 4, 5, 6, 7]
Input2 =  [9, 6, 8, 3, 7]
Input3 = [6, 9, 2, 5, 1, 4]

def solution(Input):
    length = len(Input)
    for i in range(1,length-1,2):
        if Input[i-1]>Input[i] and Input[i-1]>Input[i+1]:
            mx = i-1
        elif Input[i]>Input[i-1] and Input[i]>Input[i+1]:
            mx = i
        elif Input[i+1]>Input[i] and Input[i+1]>Input[i]:
            mx = i+1
        temp = Input[i]
        Input[i] = Input[mx]
        Input[mx] = temp
    return Input

if __name__ =="__main__":
    print(solution(Input1))
    print(solution(Input2))
    print(solution(Input3))
