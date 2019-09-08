words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

def solution(words, queries):
    answer = []
    dp =dict()

    for query in queries:
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
