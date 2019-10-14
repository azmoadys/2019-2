Input1 = [1, 2, 3, 4, 4]
Input2 = [1, 2, 3, 4, 2]

def solution(Input):
    length = len(Input)
    expect = (length-1)*length/2
    total = 0
    for i in range(length):
        total += Input[i]
    return (int)(total-expect)
        

if __name__ == '__main__':
    print(solution(Input1))
    print(solution(Input2))
