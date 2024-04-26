def solution(s):
    sm = []
    bg = []
    for c in s:
        if c.islower():
            sm.append(c)
        else:
            bg.append(c)
    sm.sort(reverse=True)
    bg.sort(reverse=True)
    
    return "".join(sm) + "".join(bg)