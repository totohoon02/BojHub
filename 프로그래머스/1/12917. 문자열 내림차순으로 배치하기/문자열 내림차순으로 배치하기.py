def solution(s):
    c = list(s)
    c.sort(reverse=True)
    return "".join(c)