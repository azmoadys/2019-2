words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

def solution(words, queries):
    answer = []
    dp =dict()
    
    len_fq = set()
    len_bq = set()

    for query in queries:
        if query[0] =='?':
            #앞이 ?
            len_bq.add(len(query)-query.count("?"))    #글자 수        
        else :
            #뒤가 ?
            len_fq.add(len(query)-query.count("?"))

    word_fdic = set()
    word_bdic = set()

    for i in len_fq:
        for word in words:
            if word[:i] in word_fdic:
                continue
            word_fdic.add(word[:i])
    for i in len_bq:
        for word in words:
            if word[len(word)-i:] in word_bdic:
                continue
            word_bdic.add(word[len(word)-i:])

    for query in queries:
        if query[0] == "?" and query.replace("?","") not in word_bdic:
            answer.append(0)
            continue
        if query[len(query)-1] == "?" and query.replace("?","") not in word_fdic:
            answer.append(0)
            continue
        if query in dp:
            answer.append(dp[query])
            continue
        else:
            dp[query] = 0
        match = 0
        checker = 0
        length = len(query)
        cnt = query.count("?")

        for word in words:
            if length !=len(word):
                continue
            if query[0] != word[0] and query[len(word)-1] != word[len(word)-1]:
                continue
            if query[0] == "?":
                if query[cnt:] == word[cnt:]:
                    match+=1
                    dp[query] = match
                else:
                    continue
            elif query[length-1] == '?':
                if query[:length-cnt] == word[:length-cnt]:
                    match+=1
                    dp[query] = match
            else:
                continue
        answer.append(match)
    return answer

if __name__ == '__main__':
    print(solution(words, queries))
