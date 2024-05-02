def solution(s):
    stack = []
    
    for bck in s:
        if bck == "(":
            stack.append(bck)
        else:
            if not stack:
                return False
            
            poped = stack.pop()
            if bck != ")":
                return False
    if stack:
        return False

    return True