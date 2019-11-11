id1 = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
ban1 = ["fr*d*", "abc1**"]

id2 = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
ban2 = ["*rodo", "*rodo", "******"]

id3 = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
ban3 = ["fr*d*", "*rodo", "******", "******"]



def check(user_ids, banned_ids,result):
    print(user_ids, banned_ids)
    if banned_ids == []:
        return 1
    else:
        for ban in banned_ids:
            ban_len = len(ban)
            pos = 0
            for user in user_ids:
                if len(user) != ban_len:
                    continue
                cnt =0
                for i in range(ban_len):
                    if ban[i] == '*':
                        cnt +=1
                        continue
                    elif ban[i] != user[i]:
                        break
                    else:
                        cnt+=1
                        continue
                if cnt == ban_len:
                    pos +=1
                    temp_id = user_ids[:]
                    temp_id.remove(user)
                    temp_ban = banned_ids[:]
                    temp_ban.remove(ban)
                    print(banned_ids, user_ids,ban, user,'temp',temp_id, temp_ban)
                    temp=check(temp_id,temp_ban,result)
                    
                    result +=temp
                    print(temp, result)
                else:
                    continue
        if pos == 0:
            return 0

def solution(user_ids, banned_ids):
    answer = 0
    result = 0
    print(check(user_ids, banned_ids,result))
    return answer

solution(id3, ban3)
