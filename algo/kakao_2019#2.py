p1 = "(()())()"
p2 = ")("
p3 = "()))((()"

def solution(p):
    answer = ''
    count = 0
    
    if p[0] == '(':
        checker = True
    else:
        checker = False

    for i in range(len(p)):
        if p[i] == '(':
            count+=1
        else:
            count-=1
        if i != 0 and count==0:
            u = p[:i+1]
            v = p[i+1:]
            #print('u : ', u)
            #print('v : ', v)
            break
    
    #print(checker)
    if checker == False:  #u가 틀렸음
        #result_u = '('*(u.count('('))+')'*(u.count('('))
        result_u = '('
        if v != '':
            result_u = result_u+solution(v)
        result_u = result_u+')'
        for i in range(1,len(u)-1):
            #print('i : ' ,i, u[i])
            if u[i] == '(':
                result_u = result_u +')'
            else:
                result_u = result_u + '('
        #result_u = result_u +')'
        #print('result_u : ', result_u)
        answer = answer + result_u #정렬된 u
    else:
        answer = answer+u
        if v != '':
            answer = answer + solution(v)
    
    #print(answer)
    return answer

if __name__ == '__main__':
    print('p1 : ',solution(p1))
    #solution(p1)
    print('p2 : ',solution(p2))
    #solution(p2)
    print('p3 : ',solution(p3))
    #solution(p3)

