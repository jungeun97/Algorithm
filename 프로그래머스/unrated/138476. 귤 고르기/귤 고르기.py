def solution(k, tangerine):
    answer = 0
    dic = {}
    for i in tangerine:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    tmp = sorted(dic.items(), key = lambda x : x[1], reverse = True)
    
    cnt = 0
    if tmp[0][1] >= k:
        return 1
    else:
        for i in tmp:
            if cnt < k:
                cnt += i[1]
                answer += 1
            else:
                break

    return answer