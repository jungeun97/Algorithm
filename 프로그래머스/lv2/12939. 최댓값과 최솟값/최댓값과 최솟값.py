from collections import deque

def solution(s):
    answer = ''
    lst = []
    stack = deque()
    for i in range(len(s)):
        if s[i] == ' ':
            while stack:
                answer += stack.popleft()
            lst.append(int(answer))
            answer = ''
        else:
            stack.append(s[i])
    if stack:
        while stack:
            answer += stack.popleft()
        lst.append(int(answer))
    answer = str(min(lst)) + ' ' + str(max(lst))
    return answer