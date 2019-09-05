# https://www.welcomekakao.com/learn/courses/30/lessons/42889
# 실패율 = 도달했지만 클리어하지 못한 사람수 / 도달한 사람들

N = 5
stages = [2,1,2,6,2,4,3,3]

def solution(N, stages):
    answer =[]
    p_ans = []
    fail = dict()
    dic = dict()
    num = dict()
    num[N+2] = 0
    for i in range(N+1, 0, -1):
        num[i] = stages.count(i)+num[i+1]
    #print(num)
    for i in range(1, N+2):
        dic[i]=False
    for i in range(1, N+1):
        fail[i] = 0
    #print(fail)
    #print(dic)
    for i in stages:
        #print(i)
        if i > N:
            continue
        if dic[i]==False:
            temp = stages.count(i)/num[i]
            fail[i] = temp
            dic[i] = True
        else:
            continue
    #print(fail)
    p_ans = sorted(fail.items(), key=lambda x:x[1], reverse = True)
    #print(p_ans)
    for i in range(0, N):
        #print(i)
        #print(p_ans[i][0])
        answer.append(p_ans[i][0])
    
    #print(answer)
    return answer

if __name__ =='__main__':
    solution(N, stages)
