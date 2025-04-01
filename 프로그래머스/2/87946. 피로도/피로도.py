from itertools import permutations

def solution(k, dungeons):
    travels = []
    pmt = list(permutations(range(len(dungeons)), len(dungeons)))
    
    for p in pmt:
        fatigue = k
        count = 0
        
        for idx in list(p):
            if fatigue >= dungeons[idx][0]:
                count += 1
                fatigue -= dungeons[idx][1]

        travels.append(count)
        
    return max(travels)