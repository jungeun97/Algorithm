def solution(s):
    answer = True
    stack = []
    for i in range(len(s)):
        if not stack:
            if s[i] == ')':
                answer = False
                break
            else:
                stack.append(s[i])
        else:
            if stack[-1] == '(':
                if s[i] == ')':
                    stack.pop()
                else:
                    stack.append(s[i])
    if stack:
        answer = False
                
    return answer