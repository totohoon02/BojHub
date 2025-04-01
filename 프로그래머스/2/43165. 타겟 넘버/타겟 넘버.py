def solution(numbers, target):
    answer = 0
    bfs = [0]
    
    for num in numbers:
        temp = []
        
        for l in bfs:
            temp.append(l + num)
            temp.append(l - num)
        
        bfs = temp
        
    for l in bfs:
        if l == target:
            answer += 1
            
    return answer