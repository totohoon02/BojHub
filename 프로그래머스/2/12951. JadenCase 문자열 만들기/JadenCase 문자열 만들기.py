def solution(s):
    answer = s[0].upper() if s[0].isalpha() else s[0]
    
    prev = ""
    for i in range(1, len(s)):
        cur = s[i]
        
        if prev == " " and cur.isalpha():
            answer += cur.upper()
        else:
            answer += cur.lower()
        
        prev = cur
    
    return answer