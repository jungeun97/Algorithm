from collections import deque

def solution(s):
    answer = ''
    tmp = ''
    stack = deque()
    for i in range(len(s)):
        if s[i] != ' ':
            stack.append(s[i])
        else:
            while stack:
                tmp += stack.popleft()
            answer += tmp.capitalize() + ' '
            tmp = ''
    if stack:
        while stack:
            tmp += stack.popleft()
        answer += tmp.capitalize()
    return answer