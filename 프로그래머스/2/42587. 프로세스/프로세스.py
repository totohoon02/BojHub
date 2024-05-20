from collections import deque

def solution(priorities, location):
    answer = 0
    p = deque(priorities)
    
    while True:
        cur = p.popleft()
        
        if not p:
            return answer + 1
        
        if cur >= max(p):
            answer += 1
            
            if location == 0:
                break
        else:
            p.append(cur)
        
        location -= 1
        
        if location == -1:
            location = len(p) - 1
        
    
    return answer