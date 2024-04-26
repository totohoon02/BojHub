def solution(name, yearning, photo):
    answer = []
    d = dict()
    
    # init dict
    for i, n in enumerate(name):
        d[n] = yearning[i]
    
    
    # calc score
    for p in photo:
        score = 0
        for n in p:
            if n in d:
                score += d[n]
        answer.append(score)
    
    return answer