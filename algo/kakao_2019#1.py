# https://tech.kakao.com/2018/09/21/kakao-blind-recruitment-for2019-round-1/

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
import sys

def solution(record):
    answer = []
    dic = dict()
    number = 0
    for words in record:
        word = words.split() # [0]==command / [1]==UID / [2]==Nickname
        if word[0] == 'Enter':
            dic.update({word[1]:word[2]}) # UID:Nickname
        elif word[0] == 'Change':
            temp = dic[word[1]]
            dic.update({word[1]:word[2]})
        #elif word[0] =='Leave':
            #answer.append(1)
    for words in record:
        word = words.split()
        if word[0] =='Enter':
            answer.append(dic[word[1]]+"님이 들어왔습니다.")
        if word[0] == 'Leave':
            answer.append(dic[word[1]]+"님이 나갔습니다.")
            
#    print(dic)
    print(answer)
    return answer

if __name__ == '__main__':
    solution(record)
