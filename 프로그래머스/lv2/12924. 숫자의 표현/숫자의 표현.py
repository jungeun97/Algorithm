def solution(n):
    value = 0
    cnt = 0
    k = 1
    while True:
        if k == n+1:
            break
        for i in range(k, n+1):
            value += i
            if value == n:
                cnt += 1
            elif value > n:
                value = 0
                break
        value = 0
        k += 1
        
    return cnt
