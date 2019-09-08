words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

def solution(words, queries):
    answer = []
    
    len_fq = set()
    len_bq = set()

    for query in queries:
        if query.count('?') == 0: #? 없음
            continue
        if query.count("?") != 0 and query[0] != '?' and query[len(query)-1] != '?': #중간에 ?
            continue
        #if issubset({len(query)-query.count("?")})

        if query[0] =='?':
            #앞이 ?
            len_bq.add(len(query)-query.count("?"))    #글자 수        
        else :
            #뒤가 ?
            len_fq.add(len(query)-query.count("?"))

    word_fdic = dict()
    word_bdic = dict()


    for i in len_fq:
        word_fdic[i] = []
        for word in words:
            word_fdic[i].append(word[:i])
    for i in len_bq:
        word_bdic[i] = []
        for word in words:
            word_bdic[i].append(word[len(word)-i:])

    print(word_fdic)
    print()
    print(word_bdic)


    for query in queries:
        if query.count('?') == 0: #? 없음
            continue
        if query.count("?") != 0 and query[0] != '?' and query[len(query)-1] != '?': #중간에 ?
            continue 

        match = 0
        if query[0] =='?':
            temp_q = query[query.count("?"):]
            for i in word_fdic[len(temp_q)]:
                if i == temp_q:
                    match += 1
                else:
                    continue
        else :
            temp_q = query[:len(query)-query.count('?')]
            for i in word_bdic[len(temp_q)]:
                if i == temp_q:
                    match+=1
                else:
                    continue
        answer.append(match)
            

    return answer

if __name__ == '__main__':
    print(solution(words, queries))

