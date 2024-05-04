def solution(s):
    l = list(s)
    stack = []

    for c in l:
        if stack and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)
    
    if stack:
        return 0
        
    return 1