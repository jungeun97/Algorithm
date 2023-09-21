def solution(n, times):
    answer = 0
    l = len(times)
    times.sort()
    s = min(times)
    e = min(times) * n
    while s <= e:
        cnt = 0
        mid = (s + e) // 2
        
        for i in range(l):
            cnt += mid // times[i]
        
        if cnt < n:
            s = mid + 1
        else:
            e = mid - 1
            answer = mid
    return answer